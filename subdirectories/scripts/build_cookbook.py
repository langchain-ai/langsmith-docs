import os
import re
from pathlib import Path
from shutil import copy2

import nbformat
from nbconvert import MarkdownExporter
from tqdm import tqdm

_REPO_ROOT = "https://github.com/langchain-ai/langsmith-cookbook"


def convert_notebooks_to_markdown(root_path: str):
    """Convert all Jupyter notebooks in the directory to Markdown."""
    exporter = MarkdownExporter()
    for dirpath, _, filenames in tqdm(os.walk(root_path)):
        for file in filenames:
            if file.endswith(".ipynb"):
                file_path = os.path.join(dirpath, file)
                with open(file_path, "r", encoding="utf-8") as notebook_file:
                    notebook = nbformat.read(notebook_file, as_version=4)
                    markdown, _ = exporter.from_notebook_node(notebook)
                    md_file_path = os.path.join(dirpath, file.replace(".ipynb", ".md"))
                    with open(md_file_path, "w", encoding="utf-8") as md_file:
                        md_file.write(markdown)


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

The LangSmith Cookbook offers hands-on code examples to inspire and assist in your projects. While we've incorporated summaries and overviews from the READMEs here, the full code resides in our [GitHub repository](https://github.com/langchain-ai/langsmith-cookbook). We suggest running the code by forking or cloning the repository.

**What's Inside?**
This repository is your practical guide to maximizing LangSmith. As a tool, LangSmith empowers you to debug, evaluate, test, and oversee your LLM applications seamlessly. These recipes dive deeper than the standard documentation, presenting real-world scenarios for you to adapt and implement.

**Your Input Matters**
We're always evolving. If there's a specific use case or pattern you want to see or if you'd like to contribute, raise a GitHub issue or reach out to the LangChain development team. Your feedback helps everyone!

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
