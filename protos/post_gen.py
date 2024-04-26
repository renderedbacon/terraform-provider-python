#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
from re import compile, Match, Pattern, MULTILINE


def main():
    parser = ArgumentParser()
    parser.add_argument("--python_out", required=True)
    parser.add_argument("--pyi_out", required=False)
    parser.add_argument("--grpc_python_out", required=True)
    parser.add_argument("--proto_file", required=True)
    args = parser.parse_args()

    proto_file = Path(args.proto_file)
    python_out = Path(args.python_out) / f"{proto_file.stem}_pb2.py"
    grpc_python_out = Path(args.grpc_python_out) / f"{proto_file.stem}_pb2_grpc.py"

    proto_module: str = f"{python_out.stem}"
    proto_alias: str = proto_module.replace("_", "__")

    # update class imports

    import_classes_regex: Pattern = compile(f"(?P<module>{proto_alias}\\.)(?P<import>[^\\.]+)\\.")
    grpc_file_text: str = grpc_python_out.read_text()

    class_imports: set[str] = set()
    m: Match
    for m in import_classes_regex.finditer(grpc_file_text):
        module: str = m.group("module")
        import_class: str = m.group("import")
        class_imports.add(import_class)
        grpc_file_text = grpc_file_text.replace(f"{module}{import_class}.", f"{import_class}.", 1)

    # update import statement

    import_regex: Pattern = compile(f"import {proto_module} as {proto_alias}")
    m = import_regex.search(grpc_file_text)
    if m:
        grpc_file_text = grpc_file_text.replace(m.group(), f"from .{proto_module} import (\n    {",\n    ".join(class_imports)},\n)")

    # update add servicer to server method signature
    # def add_ProviderServicer_to_server(servicer: ProviderServicer, server: grpc.Server):
    servicer_to_server_regex: Pattern = compile(r"def add_(?P<servicer>[^_]+)_to_server\(servicer, server\):", flags=MULTILINE)
    m = servicer_to_server_regex.search(grpc_file_text)
    if m:
        servicer: str = m.group("servicer")
        grpc_file_text = grpc_file_text.replace(
            f"def add_{servicer}_to_server(servicer, server):",
            f"def add_{servicer}_to_server(servicer: {servicer}, server: grpc.Server):",
        )

    # write back to file

    print(f"Writing to {grpc_python_out}")
          
    grpc_python_out.write_text(grpc_file_text)

if __name__ == "__main__":
    main()
