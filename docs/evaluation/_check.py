import re

with open('quickstart.mdx', 'r') as file:
    all_mdx_content = file.read() 

code_block_pattern = re.compile(r'content: `([^`]*)`', re.DOTALL)

by_code_tabs = all_mdx_content.split("<CodeTabs")
steps = []
for mdx_content in by_code_tabs:
    python_code_blocks = code_block_pattern.findall(mdx_content)

    formatted = []
    for index, code in enumerate(python_code_blocks, start=1):
        if ";" in code or "@langchain" in code or "pip install" in code:
            # Silly.
            continue
        formatted_code = code.strip().strip('"').strip("'").replace("\\n", "\n")
        print(f"Python Code Block {index}:\n{formatted_code}\n---\n")
        formatted.append(formatted_code)
    if formatted:
        steps.append(formatted)

