
# FolderUtil

## Introduction

FolderUtil is a versatile utility tool designed to assist with everyday folder and file management tasks. It operates directly from the command line and can also be accessed from the context menu if enabled.

## Features

- **Batch Rename**: Rename files in a folder with optional prefix, suffix, and numbering.
- **Dump Folder**: List folder contents, write the output to a file, and apply various filters and view options.
  - Optional Arguments:
    - `--copytoclipboard`: Copy the output to the clipboard.
    - `--treeview`: Enable tree view for the folder dump.
    - `--filtercommon`: Filter out common unnecessary files.
- **File Count**: Get the number of files in a folder.
- **Extension Count**: Count files by their extensions.

## Requirements

- Python 3.x
- PowerShell (for Windows context menu integration)

## Warning

⚠️ Tinkering with the system PATH or Windows Registry could lead to unexpected behavior. Proceed with caution. I do not take responsibility for any damage or loss.

## Installation

1. Clone the GitHub repository.
2. Run `compile_util.bat` to compile the Python script into an executable.
3. Optionally, run `add_to_path.ps1` to add the utility to your system PATH, enabling you to invoke it by typing `FolderUtil` in the command line.
4. Optionally, run `add_to_folder_context_menu.ps1` as an administrator to add a right-click context menu item in Windows Explorer, which will allow you to dump folder contents easily.

## Usage

### Batch Rename
```bash
FolderUtil -ur --prefix="new_" --suffix="_old"
```

### Dump Folder
```bash
FolderUtil -ud --copytoclipboard --treeview --filtercommon
```

### File Count
```bash
FolderUtil -uda
```

### Extension Count
```bash
FolderUtil -udae
```

## Contributing

Feel free to fork the project, make changes, and create pull requests.

## License

MIT License
