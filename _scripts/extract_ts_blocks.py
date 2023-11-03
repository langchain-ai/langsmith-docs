import re
from pathlib import Path
from typing import Tuple


def extract_code_blocks(mdx_file: str) -> list[str]:
    """
    Extract all TypeScript code blocks from an MDX file.

    :param mdx_file: Path to the MDX file
    :return: A list of code blocks
    """
    with open(mdx_file, "r") as file:
        content = file.read()
        # Pattern to match code inside TypeScriptBlock(\``) from code tabs
        code_blocks = re.findall(
            r"TypeScriptBlock\(`(.*?)`(?:,|\))", content, re.DOTALL
        )
        code_blocks = [
            code_block.replace("\\n", "\n").replace("\\\\", "\\")
            for code_block in code_blocks
            if "<run_id>" not in code_block
            and "<your_" not in code_block
            and "YOUR_" not in code_block
        ]
        return code_blocks


def transform_imports(code_block: str) -> Tuple[str, str]:
    """
    Transform static import statements to dynamic imports in TypeScript.

    :param code_block: The code block to transform
    :return: The code block with transformed import statements
    """
    lines = code_block.split("\n")
    import_lines = []
    other_lines = []
    import_block = False
    for line in lines:
        if line.startswith("import "):
            if "{" in line:
                import_block = True
            import_lines.append(line)
        elif import_block:
            import_lines[-1] += line + "\n"
        else:
            other_lines.append(line)
        if "}" in line:
            import_block = False
    return "\n".join(import_lines), "\n".join(other_lines)


def add_boilerplate(code_block: str) -> str:
    """
    Add boilerplate code to the code block.

    :param code_block: The code block to transform
    :return: The code block with boilerplate code
    """
    if ("chain.invoke" in code_block or "configuredChain.invoke" in code_block) and "const chain = " not in code_block:
        code_block = (
            """import { ChatOpenAI } from "langchain/chat_models/openai";
import {
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
} from "langchain/prompts";

const chatPrompt = ChatPromptTemplate.fromPromptMessages([
  HumanMessagePromptTemplate.fromTemplate("{query}"),
]);

const chain = chatPrompt.pipe(new ChatOpenAI());
"""
            + code_block
        )
    return code_block


def write_jest_tests(code_blocks: list[str], output_dir: str) -> None:
    """
    Write Jest unit tests to a file for each TypeScript code block.

    :param code_blocks: List of code blocks to test
    :param output_file: Path to the output file
    """
    for index, code_block in enumerate(code_blocks):
        output_file = f"{output_dir}/test_code_block_{index}.test.ts"
        with open(output_file, "w") as file:
            code_block = add_boilerplate(code_block)
            imports, transformed_code = transform_imports(code_block)
            if imports:
                file.write(imports + "\n")
            indented_code = "\n".join(
                ["    " + line for line in transformed_code.strip().split("\n")]
            )
            test_code = f"""
test('test_code_block_{index}', async () => {{
{indented_code}
}});
"""
            file.write(test_code)
        print(f"Tests written to {output_file}")


def main(mdx_file: str, output_dir: str) -> None:
    """
    Main function to extract TypeScript code blocks from MDX and write to Jest file.

    :param mdx_file: Path to the MDX file
    :param output_file: Path to the output file
    """
    code_blocks = extract_code_blocks(mdx_file)
    write_jest_tests(code_blocks, output_dir)


if __name__ == "__main__":
    root = Path(__file__).parent.parent.absolute()
    files = ["tracing/tracing-faq.mdx"]
    for file in files:
        stem = Path(file).stem
        dest_folder = root / "tests/js_unit_tests" / Path(file).parent / stem
        # Remove recursive all files in the folder
        for f in dest_folder.glob("*"):
            f.unlink()
        dest_folder.mkdir(parents=True, exist_ok=True)
        main(
            str(root / "docs" / file),
            str(dest_folder),
        )
