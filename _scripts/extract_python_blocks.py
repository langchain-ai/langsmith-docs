import re
from pathlib import Path
import ast

class ReplaceListRunsVisitor(ast.NodeTransformer):
    def visit_Call(self, node):
        self.generic_visit(node)  # First, apply transformation to children
        if isinstance(node.func, ast.Attribute) and node.func.attr == "list_runs":
            # Wrap the original call in `list(...)`
            return ast.Call(
                func=ast.Name(id="list", ctx=ast.Load()),
                args=[node],
                keywords=[]
            )
        return node

def _call_list_on_list_runs(code_block: str):
    tree = ast.parse(code_block)
    transformer = ReplaceListRunsVisitor()
    transformed_tree = transformer.visit(tree)

    return  ast.unparse(transformed_tree)



def extract_code_blocks(mdx_file: str) -> list[str]:
    """
    Extract all code blocks from an MDX file.

    :param mdx_file: Path to the MDX file
    :return: A list of code blocks
    """
    with open(mdx_file, "r") as file:
        content = file.read()
        # Pattern to match code inside PythonBlock(\``) from code tabs
        code_blocks = re.findall(r"PythonBlock\(`(.*?)`(?:,|\))", content, re.DOTALL)
        # Assuming code blocks are enclosed between triple backticks
        code_blocks += [
            c.strip() for c in re.findall(r"```python\n(.*?)\n```", content, re.DOTALL)
        ]
        code_blocks = [
            _call_list_on_list_runs(
                code_block.replace("\\n", "\n").replace("\\\\", "\\")
            )
            for code_block in code_blocks
            # Skip because we don't have the actual UUID to run in the test.
            if "<run_id>" not in code_block
            and "<your_project>" not in code_block
            and "create_dataset" not in code_block
        ]

        return code_blocks


def write_pytest_tests(
    code_blocks: list[str], output_file: str, boilerplate: str = ""
) -> None:
    """
    Write pytest unit tests to a Python file for each code block.

    :param code_blocks: List of code blocks to test
    :param output_file: Path to the output Python file
    """
    with open(output_file, "w") as file:
        file.write("import pytest\n")
        file.write(boilerplate)
        for index, code_block in enumerate(code_blocks):
            indented_code = "\n".join(
                ["    " + line for line in code_block.split("\n")]
            )
            test_code = f"""
@pytest.mark.asyncio
async def test_code_block_{index}():
{indented_code}
"""
            file.write(test_code)


def main(mdx_file: str, output_file: str, boilerplate: str = "") -> None:
    """
    Main function to extract code blocks from MDX and write to pytest file.

    :param mdx_file: Path to the MDX file
    :param output_file: Path to the output Python file
    """
    code_blocks = extract_code_blocks(mdx_file)
    write_pytest_tests(code_blocks, output_file, boilerplate=boilerplate)
    print(f"Tests written to {output_file}")


if __name__ == "__main__":
    root = Path(__file__).parent.parent.absolute()
    files = [
        (
            "tracing/faq/querying_traces.mdx",
            """from langsmith import Client
    
client = Client()
""",
        ),
    ]
    for file, boilerplate in files:
        stem = Path(file).stem
        dest_folder = root / "tests/py_unit_tests" / Path(file).parent
        dest_folder.mkdir(parents=True, exist_ok=True)
        main(
            str(root / "docs" / file),
            str(dest_folder / f"test_{stem}.py"),
            boilerplate=boilerplate,
        )
