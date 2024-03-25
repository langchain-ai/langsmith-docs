import os
import shutil
import inspect
from pathlib import Path
import langsmith
import langsmith.evaluation


def generate_sdk_docs():
    # Set the output directory within the docs folder
    output_dir = Path(__file__).parents[1] / "docs/sdks/python"
    output_dir = Path(os.path.normpath(output_dir)).absolute()
    print(output_dir)

    # Remove the existing output directory if it exists
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)

    # Create the output directory
    os.makedirs(output_dir)

    to_render = [
        ("client", langsmith.Client),
        ("tracing", langsmith.traceable),
        ("tracing", langsmith.trace),
        ("evaluation", langsmith.evaluation.evaluate),
    ]

    # Generate documentation for langsmith exports
    for module, obj in to_render:
        doc = generate_doc(obj)
        with (output_dir / f"{module}.md").open("a") as f:
            f.write(doc)


def generate_doc(obj):
    doc = f"# {obj.__name__}\n\n"
    doc += f"{inspect.getdoc(obj)}\n\n"
    def _get_annotation(param: inspect.Parameter):
        return getattr(param.annotation, "__name__", param.annotation)
    if inspect.isclass(obj):
        # Generate documentation for class methods
        for name, method in inspect.getmembers(obj, predicate=inspect.isfunction):
            if not name.startswith("_"):
                doc += f"## {name}\n\n"
                doc += f"{inspect.getdoc(method)}\n\n"

                # Generate documentation for method parameters
                doc += "### Parameters\n\n"
                signature = inspect.signature(method)
                for param in signature.parameters.values():
                    if param.name != "self":
                        doc += f"- {param.name}: { _get_annotation(param) if param.annotation != inspect.Parameter.empty else 'Any'}\n"
                doc += "\n"

    elif inspect.isfunction(obj):
        # Generate documentation for function parameters
        doc += "## Parameters\n\n"
        signature = inspect.signature(obj)
        for param in signature.parameters.values():
            if param.name != "self":
                doc += f"- {param.name}: {_get_annotation(param)if param.annotation != inspect.Parameter.empty else 'Any'}\n"
        doc += "\n"

    return doc


if __name__ == "__main__":
    generate_sdk_docs()
