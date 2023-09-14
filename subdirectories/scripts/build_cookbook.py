import os
import re
from pathlib import Path
from shutil import copy2

import nbformat
from bs4 import BeautifulSoup
from nbconvert import MarkdownExporter
from tqdm import tqdm

_REPO_ROOT = "https://github.com/langchain-ai/langsmith-cookbook"

def convert_notebooks_to_markdown(root_path: str) -> None:
    """
    Convert all Jupyter notebooks in the directory to Markdown and save images.

    Args:
    - root_path (str): Path to the root directory containing the notebooks.
    """
    exporter = MarkdownExporter()

    # This function will be used to save the images
    def output_post_save(md, resources, **kwargs):
        for filename, data in resources.get("outputs", {}).items():
            filepath = os.path.join(resources["metadata"]["path"], filename)
            with open(filepath, "wb") as f:
                f.write(data)

    for dirpath, _, filenames in tqdm(os.walk(root_path)):
        for file in filenames:
            if file.endswith(".ipynb"):
                file_path = os.path.join(dirpath, file)
                with open(file_path, "r", encoding="utf-8") as notebook_file:
                    notebook = nbformat.read(notebook_file, as_version=4)
                    # The exporter's `from_notebook_node` function has a `resources` parameter.
                    # We can use this to specify where and how to save images.
                    resources = {
                        "metadata": {"path": dirpath}  # Set the output path for images
                    }
                    markdown, resources = exporter.from_notebook_node(
                        notebook, resources=resources
                    )

                    output_post_save(markdown, resources)
                    markdown = clean_markdown(markdown)

                    md_file_path = os.path.join(dirpath, file.replace(".ipynb", ".md"))
                    with open(md_file_path, "w", encoding="utf-8") as md_file:
                        md_file.write(markdown)

def flexible_table_replacement(markdown: str, table_str: str) -> str:
    """
    Replace the table in the markdown with the given table string using a more flexible matching.
    
    Args:
    - markdown (str): The original markdown content.
    - table_str (str): The exact table string to replace with.

    Returns:
    - str: The markdown with the table replaced.
    """
    start_of_table = "<table"
    end_of_table = "</table>"
    
    start_index = markdown.find(start_of_table)
    end_index = markdown.find(end_of_table, start_index) + len(end_of_table) if start_index != -1 else -1
    
    # If both start and end are found, replace
    if start_index != -1 and end_index != -1:
        return markdown[:start_index] + table_str + markdown[end_index:]
    else:
        return markdown

def clean_markdown(markdown: str) -> str:
    soup = BeautifulSoup(markdown, "html.parser")
    for table in soup.find_all("table"):
        md_table = html_table_to_markdown(str(table))
        markdown = flexible_table_replacement(markdown, md_table)
    markdown = remove_dataframe_styles(markdown)
    markdown = remove_stray_divs(markdown)
    return markdown

def remove_stray_divs(markdown: str) -> str:
    """
    Remove stray and empty <div> tags from the markdown content.
    
    Args:
    - markdown (str): The original markdown content.

    Returns:
    - str: The markdown without stray and empty <div> tags.
    """
    soup = BeautifulSoup(markdown, "html.parser")
    
    # Remove empty <div> tags
    for div in soup.find_all("div"):
        if not div.contents or all(isinstance(c, str) and not c.strip() for c in div.contents):
            div.extract()

    # Convert back to string and check for stray <div> tags
    cleaned_content = str(soup)
    cleaned_content = cleaned_content.replace("<div>", "").replace("</div>", "")
    
    return cleaned_content


def remove_dataframe_styles(markdown: str) -> str:
    """
    Remove style blocks related to Pandas DataFrames from the markdown content.
    
    Args:
    - markdown (str): The original markdown content.

    Returns:
    - str: The markdown without the DataFrame style blocks.
    """
    soup = BeautifulSoup(markdown, "html.parser")
    
    # Find all <style> tags with the 'scoped' attribute (commonly used by Pandas DataFrame styles)
    for style_tag in soup.find_all("style", attrs={"scoped": True}):
        style_tag.extract()  # Remove the tag from the soup object

    return str(soup)

def html_table_to_markdown(html_content: str) -> str:
    """
    Convert an HTML table into a Markdown table.

    Args:
    - html_content (str): The HTML content containing the table.

    Returns:
    - str: The Markdown representation of the table.
    """
    soup = BeautifulSoup(html_content, "html.parser")
    table = soup.find("table")

    # If no table is found, return the original content
    if not table:
        return html_content

    # Extracting headers
    headers = [th.get_text().strip() for th in table.find_all("th")]
    header_str = " | ".join(headers)

    # Creating separator
    separator = "--- | " * (len(headers) - 1) + "---"

    # Extracting rows
    rows = table.find_all("tr")[1:]  # excluding header
    row_strs = []
    for row in rows:
        row_strs.append(
            " | ".join([td.get_text().strip() for td in row.find_all("td")])
        )

    # Combining everything
    markdown_table = "\n".join([header_str, separator] + row_strs)
    return markdown_table


def move_to_docs(root_path: str, destination_path: str) -> None:
    """Move all markdown files and linked images to the docs folder."""
    img_extensions = [".png", ".jpg", ".jpeg", ".gif", ".svg"]
    for dirpath, _, filenames in tqdm(os.walk(root_path)):
        for file in filenames:
            if file.endswith(tuple([".md"] + img_extensions)):
                src = os.path.join(dirpath, file)
                dest = os.path.join(
                    destination_path, "cookbook", os.path.relpath(src, root_path)
                )

                # Adjust paths
                if file.endswith(".png"):
                    dest = dest.replace("img/", "static/")
                if file.endswith(".md"):
                    # Make the name index.md
                    dest = os.path.join(os.path.dirname(dest), "index.md")

                os.makedirs(os.path.dirname(dest), exist_ok=True)
                copy2(src, dest)

                # Adjust content in Markdown files
                if file.endswith(".md"):
                    with open(dest, "r", encoding="utf-8") as md_file:
                        content = md_file.read()

                    # If the destination path is /cookbook/index.md, this is the "overview" page.
                    # Insert metadata and an introduction.
                    if dest.endswith("/cookbook/index.md"):
                        title, rest = content.strip().split("\n", 1)
                        content = f"""---
sidebar_label: Overview
sidebar_position: 1
---
{title}

The LangSmith Cookbook offers hands-on code examples to inspire and assist in your projects.
While we've incorporated summaries and overviews from the READMEs here, the full code resides
in our [GitHub repository](https://github.com/langchain-ai/langsmith-cookbook).
We suggest running the code by forking or cloning the repository.

## Introduction
{rest}
"""
                    content = content.replace("img/", "static/")

                    def replace_relative_link(match):
                        # Extract the relative link from the match object (excluding './')
                        match_group = match.group(1)

                        if match_group.startswith("../"):
                            # For sibling or parent directory links
                            path_parts = os.path.relpath(dirpath, root_path).split(
                                os.sep
                            )
                            relative_parts = match_group.split("/")
                            while relative_parts and relative_parts[0] == "..":
                                relative_parts.pop(0)
                                path_parts.pop()
                            relative_link = "/".join(relative_parts)
                            absolute_link = os.path.join(
                                "/cookbook", *path_parts, relative_link
                            )
                        else:
                            # Convert the relative link to an absolute link
                            absolute_link = os.path.join(
                                "/cookbook",
                                os.path.relpath(dirpath, root_path),
                                match_group,
                            )

                        absolute_link = absolute_link.replace("/./", "/")
                        # If it's an absolute static link, just retain the last static/file.png part
                        if "/static/" in absolute_link:
                            return f"]({match_group})".replace("/./", "/")
                        return f"]({absolute_link})"

                    relative_link_pattern = re.compile(r"\]\((\.{1,2}/[^\)]+)\)")
                    content = relative_link_pattern.sub(replace_relative_link, content)

                    # Replace links to .py files or .ts files with
                    def replace_code_links(match):
                        # Extract the relative link from the match object (excluding './')
                        relative_link = match.group(1).lstrip("./")
                        absolute_link = (
                            os.path.join(
                                _REPO_ROOT,
                                "blob/main",
                                os.path.relpath(dirpath, root_path),
                                relative_link,
                            )
                            .replace("/./", "/")
                            .replace("/cookbook/", "/")
                        )
                        return f"]({absolute_link})"

                    code_link_pattern = re.compile(r"\]\(([^)]*\.(py|ts|txt|json))\)")
                    content = code_link_pattern.sub(replace_code_links, content)

                    def replace_md_ipynb_links(match):
                        # Extract the relative link from the match object
                        relative_link = match.group(1)
                        if "colab.research.google" in relative_link:
                            return match.group(0).replace("/./", "/")
                        parent_dir = os.path.dirname(relative_link)
                        return f"]({parent_dir})"

                    md_ipynb_pattern = re.compile(r"\]\(([^)]*\.(md|ipynb))\)")
                    content = md_ipynb_pattern.sub(replace_md_ipynb_links, content)

                    content = content.replace("<", "&lt;")
                    content = content.replace(">", "&gt;")
                    content = content.replace("/README.md)", "/)")

                    with open(dest, "w", encoding="utf-8") as md_file:
                        md_file.write(content)


if __name__ == "__main__":
    cookbook_directory = Path(__file__).parents[1] / "langsmith-cookbook"
    convert_notebooks_to_markdown(cookbook_directory)
    docs_directory = Path(__file__).parents[2] / "docs"
    move_to_docs(cookbook_directory, docs_directory)
