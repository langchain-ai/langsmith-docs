import re
import os
from typing import Tuple

def write_code_files(language_and_code_list: Tuple[str, str]) -> str:
    language = language_and_code_list[0]
    # Replace `\n` with actual newlines.
    code = language_and_code_list[1].replace('\\n', """
""").replace('\\`', '`')

    if language == "python":
        file_extension = ".py"
    elif language == "typescript":
        file_extension = ".ts"
    else:
        # Return the code, unmodified if the language is not python or typescript
        return code
        
    tmp_folder = "tmp"
    # create a new folder if it doesn't exist
    os.makedirs(tmp_folder, exist_ok=True)

    formatted_code = ""
    file_name = f"code_block_{len(os.listdir(tmp_folder))}_{language}{file_extension}"
    file_path = os.path.join(tmp_folder, file_name)
    absolute_path = os.path.abspath(file_path)

    # Write the un-formatted code to a file
    with open(absolute_path, "w") as file:
        file.write(code)

    ts_format_cmd = "yarn prettier --write"
    py_format_cmd = "ruff format"

    if language == "typescript":
        os.system(f"{ts_format_cmd} {absolute_path}")
    elif language == "python":
        os.system(f"{py_format_cmd} {absolute_path}")

    # Read the formatted code from the file and return it
    with open(absolute_path, "r") as file:
        formatted_code = file.read()

    formatted_code = formatted_code.replace('`', '\\`')

    # Cleanup, delete the file
    os.remove(absolute_path)

    return formatted_code

def extract_codeblock_props(mdx_content: str) -> str:
    code_str_pattern = r'content: `(.*?)(?<![^\\\\]\\\\)`,'
    code_tabs_pattern = r'<CodeTabs\s+tabs=\{(.*?)\}\s*(groupId=".*?")?\s*^/>'
    language_pattern = r'language: "(\w+)"'

    matches = re.findall(code_tabs_pattern, mdx_content, re.DOTALL + re.MULTILINE)

    for match in matches:
        code_obj = match[0]
        language_matches = re.findall(language_pattern, code_obj, re.DOTALL + re.MULTILINE)
        code_matches = re.findall(code_str_pattern, code_obj, re.DOTALL + re.MULTILINE)

        if len(language_matches) == 0 or len(code_matches) == 0:
            print("No matches found")
            continue
        if len(language_matches) != len(code_matches):
            raise ValueError("Number of languages and code blocks do not match")

        language_and_code_list = list(zip(language_matches, code_matches))
        # Iterate over the list of tuples, format the code and replace the
        # unformatted code with the formatted code.
        for language_and_code in language_and_code_list:
            formatted_code = write_code_files(language_and_code)
            code = language_and_code[1]
            mdx_content = mdx_content.replace(code, formatted_code)
    
    return mdx_content


def test_extract_codeblock_props():
    # read all .mdx files in a directory
    directory = "/Users/bracesproul/code/lang-chain-ai/langsmith-docs/docs"
    mdx_files = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".mdx"):
                file_path = os.path.join(root, file)
                mdx_files.append(file_path)

    for file_path in mdx_files:
        new_content = ""

        with open(file_path, "r") as file:
            content = file.read()
            new_content = extract_codeblock_props(content)
        
        # re-write the file with the new content
        with open(file_path, "w") as file:
            file.write(new_content)

test_extract_codeblock_props()
