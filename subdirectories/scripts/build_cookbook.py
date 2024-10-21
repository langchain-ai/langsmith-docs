import os
import re
from pathlib import Path
from shutil import copy2

import nbformat
from bs4 import BeautifulSoup
from nbconvert import MarkdownExporter
from nbconvert.preprocessors import Preprocessor
from traitlets.config import Config
from tqdm import tqdm
from black import format_str, Mode
from html.parser import HTMLParser

_REPO_ROOT = "https://github.com/langchain-ai/langsmith-cookbook"

black_mode = Mode()


# Cell
class HTMLdf(HTMLParser):
    """HTML Parser that finds a dataframe."""

    df = False
    scoped = False

    def handle_starttag(self, tag, attrs):
        if tag == "style":
            for k, v in attrs:
                if k == "scoped":
                    self.scoped = True

    def handle_data(self, data):
        if ".dataframe" in data and self.scoped:
            self.df = True

    def handle_endtag(self, tag):
        if tag == "style":
            self.scoped = False

    @classmethod
    def search(cls, x):
        parser = cls()
        parser.feed(x)
        return parser.df


class Black(Preprocessor):
    """Format code that has a cell tag `black`"""

    def preprocess_cell(self, cell, resources, index):
        tags = cell.metadata.get("tags", [])
        if cell.cell_type == "code" and "black" in tags:
            cell.source = format_str(src_contents=cell.source, mode=black_mode).strip()
        return cell, resources


def clean_markdown(markdown: str, all_attrs: bool = False) -> str:
    soup = BeautifulSoup(markdown, "html.parser")
    for table in soup.find_all("table"):
        md_table = html_table_to_markdown(str(table))
        markdown = flexible_table_replacement(markdown, md_table)
    markdown = remove_dataframe_styles(markdown, all_attrs=all_attrs)
    markdown = remove_stray_divs(markdown)
    return markdown


class HTMLEscape(Preprocessor):
    """
    Place HTML in a codeblock and surround it with a <HTMLOutputBlock> component.
    """

    def preprocess_cell(self, cell, resources, index):
        if cell.cell_type == "code":
            for o in cell.outputs:
                if o.get("data") and o["data"].get("text/html"):
                    cell.metadata.html_output = True
                    html = o["data"]["text/html"]
                    if HTMLdf.search(html):
                        cell.metadata.html_center = False
                        o["data"]["text/html"] = clean_markdown(html.strip())
                    else:
                        cell.metadata.html_center = True
                        o["data"]["text/html"] = "```html\n" + html.strip() + "\n```"
        return cell, resources


def add_github_backlink(content: str) -> str:
    """Inserts the 'Open In GitHub' shield link into the content after the Collab link."""

    # Match the Collab link and extract the GitHub path
    collab_link_pattern = r"(\[!\[Open In Collab\]\(.*\)\]\(https:/?/colab\.research\.google\.com/github/([^\)]*)\))"
    match = re.search(collab_link_pattern, content)

    if not match:
        return content
    github_path = match.group(2)
    github_base = "https://github.com/"
    github_shield = f"https://img.shields.io/badge/GitHub-View%20source-green.svg"
    github_link = f"[![Open In GitHub]({github_shield})]({github_base}{github_path})"

    # Insert the GitHub link after the Collab link
    new_content = content[: match.end(1)] + " " + github_link + content[match.end(1) :]
    return new_content


def get_mdx_exporter():
    """A mdx notebook exporter which composes many pre-processors together."""
    # TODO: Combine with other ad-hoc logic
    c = Config()
    pp = [Black, HTMLEscape]
    c.MarkdownExporter.preprocessors = pp
    return MarkdownExporter(config=c)


def convert_notebooks_to_markdown(root_path: str) -> None:
    """
    Convert all Jupyter notebooks in the directory to Markdown and save images.

    Args:
    - root_path (str): Path to the root directory containing the notebooks.
    """
    exporter = get_mdx_exporter()

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
    end_index = (
        markdown.find(end_of_table, start_index) + len(end_of_table)
        if start_index != -1
        else -1
    )

    # If both start and end are found, replace
    if start_index != -1 and end_index != -1:
        return markdown[:start_index] + table_str + markdown[end_index:]
    else:
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
        if not div.contents or all(
            isinstance(c, str) and not c.strip() for c in div.contents
        ):
            div.extract()

    # Convert back to string and check for stray <div> tags
    cleaned_content = str(soup)
    cleaned_content = cleaned_content.replace("<div>", "").replace("</div>", "")

    return cleaned_content


def remove_dataframe_styles(markdown: str, all_attrs: bool = False) -> str:
    """
    Remove style blocks related to Pandas DataFrames from the markdown content.

    Args:
    - markdown (str): The original markdown content.

    Returns:
    - str: The markdown without the DataFrame style blocks.
    """
    soup = BeautifulSoup(markdown, "html.parser")

    # Find all <style> tags with the 'scoped' attribute (commonly used by Pandas DataFrame styles)
    attrs = {"scoped": True} if not all_attrs else None
    for style_tag in soup.find_all("style", attrs=attrs):
        style_tag.extract()

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


def replace_brackets(content: str) -> str:
    # Search through a conent string and parse <> to &lt; and &gt;
    in_code_block = False
    new_content = ""
    for line in content.split("\n"):
        if line.startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block:
            # TODO: Handle single backticks
            line = line.replace("<", "&lt;")
            line = line.replace(">", "&gt;")
        new_content += line + "\n"
    return new_content


def replace_dead_readme_links(content: str) -> str:
    # The readmes are mapped to index.md which are mapped to the parent directory
    # by docusaurus.
    # The pattern checks that the link does not start with "http:" or "https:",
    # and then replaces the ending "/README.md)"
    pattern = r"\((?!http:|https:).*?(/README\.md\))"
    return re.sub(pattern, "(/)", content)

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
                if file.endswith((".png", ".jpg", ".jpeg", ".gif", ".svg")):
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
                                "/old/cookbook", *path_parts, relative_link
                            )
                        else:
                            # Convert the relative link to an absolute link
                            absolute_link = os.path.join(
                                "/old/cookbook",
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
                        if relative_link.startswith("http"):
                            return match.group(0)
                        parent_dir = os.path.normpath(os.path.dirname(relative_link))
                        return f"]({parent_dir})"

                    # Skip markdown comments
                    content = re.sub(r"^\s*<!--.*?-->", "", content, flags=re.MULTILINE)
                    # Bad sidebar ampersands
                    content = re.sub(
                        r"(^#\s+.*?)(\&amp;)(.*?$)",
                        r"\1&\3",
                        content,
                        flags=re.MULTILINE,
                    )
                    # Fix relative links to .md or .ipynb files
                    md_ipynb_pattern = re.compile(r"\]\(([^)]*\.(md|ipynb))\)")
                    content = md_ipynb_pattern.sub(replace_md_ipynb_links, content)
                    content = replace_brackets(content)
                    content = replace_dead_readme_links(content)
                    content = add_github_backlink(content).strip()

                    with open(dest, "w", encoding="utf-8") as md_file:
                        md_file.write(content)


if __name__ == "__main__":
    cookbook_directory = Path(__file__).parents[1] / "langsmith-cookbook"
    convert_notebooks_to_markdown(cookbook_directory)
    # NOTE: the cookbooks directory is only used in version 1.0 of docs and should thus
    #       only build into this directory
    docs_directory = Path(__file__).parents[2] / "versioned_docs" / "old"
    move_to_docs(cookbook_directory, docs_directory)
