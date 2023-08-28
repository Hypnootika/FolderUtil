import argparse
from collections import Counter
from datetime import datetime
from pathlib import Path

import pyperclip


def write_and_copy(output, copytoclipboard, file_name="output.txt", **kwargs):
    # Add extra information about the current options
    extra_info = "\n".join([f"{key}: {value}" for key, value in kwargs.items()])
    if extra_info:
        extra_info = f"Options:\n{extra_info}\n\n"
        output = extra_info + output

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"{timestamp}_{file_name}"
    with open(file_name, "w") as file:
        file.write(output)
    if copytoclipboard:
        pyperclip.copy(output)
        print(f"Output written to {file_name} and copied to clipboard.")
    else:
        print(f"Output written to {file_name}.")


def batch_rename(path, prefix="", suffix="", numerically=False):
    output = "Renaming completed.\n"
    for idx, file in enumerate(path.iterdir()):
        if file.is_file():
            ext = file.suffix
            new_name = prefix + (str(idx) if numerically else file.stem) + suffix + ext
            file.rename(path / new_name)
            output += f"Renamed {file.name} to {new_name}\n"
    write_and_copy(output, "batch_rename.txt")


def dump_folder(
    path,
    copytoclipboard=False,
    no_extension=False,
    only_extensions=False,
    treeview=True,
    filter_common=True,
):
    output = ""
    common_files = [".idea", ".gitignore", "build", "venv"]

    def walk_directory(directory, level=0):
        nonlocal output
        indent = " " * 2 * level

        if filter_common and directory.name in common_files:
            return

        if treeview or level == 0:
            output += f"{indent}{directory.name}/\n"

        for item in directory.iterdir():
            if item.is_dir():
                if not treeview:  # Include directories for -ud
                    output += f"{indent}  {item.name}/\n"
                walk_directory(item, level + 1)
            else:
                if filter_common and item.name in common_files:
                    continue

                if only_extensions:
                    output += f"{indent}  {item.suffix}\n"
                elif no_extension:
                    output += f"{indent}  {item.stem}\n"
                else:
                    output += f"{indent}  {item.name}\n"

    walk_directory(path)
    write_and_copy(
        output,
        copytoclipboard=copytoclipboard,
        file_name="dump_folder.txt",
        TreeView=treeview,
        FilterCommon=filter_common,
    )


def dump_amount(path):
    amount = sum(1 for _ in path.rglob("*"))
    output = f"Number of files in folder {path}: {amount}\n"
    write_and_copy(output, "dump_amount.txt")


def dump_amount_extensions(path):
    extensions_count = Counter()
    output = f"Number of file extensions in folder {path}:\n"
    for file in path.rglob("*"):
        extensions_count[file.suffix] += 1
    for ext, count in extensions_count.items():
        output += f"{ext}: {count}\n"
    write_and_copy(output, "dump_amount_extensions.txt")


def main():
    parser = argparse.ArgumentParser(description="Utility script for daily tasks.")
    parser.add_argument(
        "-ud",
        "--dumpfolder",
        action="store_true",
        help="Display the contents of the current folder",
    )
    parser.add_argument(
        "-c",
        "--copytoclipboard",
        action="store_true",
        help="Copy the output to clipboard",
    )
    parser.add_argument(
        "-udtv",
        "--treeview",
        action="store_true",
        help="Enable tree view for folder dump",
    )

    parser.add_argument(
        "-udfc",
        "--filtercommon",
        action="store_true",
        help="Filter out common unnecessary files",
    )

    parser.add_argument(
        "-udne",
        "--dumpnoextension",
        action="store_true",
        help="Display the folder contents without extensions",
    )
    parser.add_argument(
        "-udoe",
        "--dumponlyextensions",
        action="store_true",
        help="List only the file extensions",
    )
    parser.add_argument(
        "-uda",
        "--dumpamount",
        action="store_true",
        help="Display the amount of files in the folder",
    )
    parser.add_argument(
        "-udae",
        "--dumpamountextensions",
        action="store_true",
        help="Display the amount of extensions in the folder",
    )
    parser.add_argument(
        "-ur",
        "--rename",
        nargs="?",
        const=True,
        help="Rename files in the folder (options: --prefix, --suffix, --numerically)",
    )

    parser.add_argument(
        "-upr", "--prefix", type=str, default="", help="Prefix for renaming"
    )
    parser.add_argument(
        "-usu", "--suffix", type=str, default="", help="Suffix for renaming"
    )
    parser.add_argument(
        "-unu", "--numerically", action="store_true", help="Numerical renaming"
    )

    args = parser.parse_args()
    current_path = Path.cwd()

    if args.dumpfolder:
        dump_folder(
            current_path,
            treeview=args.treeview,
            filter_common=args.filtercommon,
            copytoclipboard=args.copytoclipboard,
        )

    if args.dumpnoextension:
        dump_folder(current_path, no_extension=True)
    if args.dumponlyextensions:
        dump_folder(current_path, only_extensions=True)
    if args.dumpamount:
        dump_amount(current_path)
    if args.dumpamountextensions:
        dump_amount_extensions(current_path)
    if args.rename:
        batch_rename(
            current_path,
            prefix=args.prefix,
            suffix=args.suffix,
            numerically=args.numerically,
        )


if __name__ == "__main__":
    main()
