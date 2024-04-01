from pathlib import Path
import re


qs = Path(__file__).parents[1] / "docs/evaluation/quickstart.mdx"
test_directory = Path(__file__).parents[1] / "tests/py_unit_tests"
test_directory.mkdir(parents=True, exist_ok=True)
test_file = test_directory / "test_evals_quickstart.py"
# Assuming mdx_content contains your MDX file content
with qs.open("r") as file:
    all_mdx_content = file.read()

# Regular expression to find code blocks within `content: ````
code_block_pattern = re.compile(r"content: `([^`]*)`", re.DOTALL)

# Find all matches
by_code_tabs = all_mdx_content.split("<CodeTabs")
steps = []
for mdx_content in by_code_tabs:
    python_code_blocks = code_block_pattern.findall(mdx_content)

    # Process each match
    formatted = []
    for index, code in enumerate(python_code_blocks, start=1):
        if ";" in code or "@langchain" in code or "pip install" in code:
            # Silly.
            continue
        # Optionally, strip leading and trailing whitespace and any quote characters
        formatted_code = code.strip().strip('"').strip("'").replace("\\n", "\n")
        formatted.append(formatted_code)
    if formatted:
        steps.append(formatted)


with test_file.open("w") as file:
    file.write("import pytest\n")
    file.write('dataset_name = "Rap Battle Dataset"' + "\n")
    for i, (first, second) in enumerate(zip(steps[0], steps[1])):
        combined = first + "\n" + second
        indented_code = "\n".join(["    " + line for line in combined.split("\n")])
        test_code = f"""
def test_code_block_{i}():
{indented_code}
"""
        file.write(test_code)
        file.write("\n")
