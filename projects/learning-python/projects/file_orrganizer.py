# ### 12. File organizer / deduplicator
# Tidy a messy folder.
# - **Requirements:** given a directory, move files into subfolders by extension
#   (`images/`, `docs/`, …); detect duplicate files by content hash and report
#   them; run in `--dry-run` mode that only prints what it *would* do.
# - **You'll learn:** `pathlib`, `shutil`, `hashlib`, `argparse`, dry-run patterns.
# - **Stretch:** undo log so a move can be reversed.

from pathlib import Path
import sys
import json


def get_target_directory(user_input):
    path = Path(user_input).resolve()

    if not path.exists():
        print(f"Error: {user_input} does not exist")
        return False

    if not path.is_dir():
        print(f"Error: {user_input} is not a directory")
        return False

    return path


def read_files_in_directory(target_path, recursive=False):
    if recursive:
        files = [f for f in target_path.rglob("*") if f.is_file()]
    else:
        files = [f for f in target_path.iterdir() if f.is_file()]
    return files


def organize_by_extension(working_dir, dry_run=False):
    files = read_files_in_directory(working_dir)

    extensions = {}
    for file in files:
        ext = file.suffix.lstrip(".") or "no_extension"
        if ext not in extensions:
            extensions[ext] = []
        extensions[ext].append(file)

    moves = []
    for ext, file_list in extensions.items():
        folder_name = ext
        folder_path = working_dir / folder_name
        folder_path.mkdir(exist_ok=True)

        for file in file_list:
            destination = folder_path / file.name
            if dry_run:
                print(f"[DRY-RUN] Would move: {file.name} → {folder_name}/")
            else:
                file.rename(destination)
                moves.append({"from": str(file), "to": str(destination)})
                print(f"Moved: {file.name} → {folder_name}/")

    if not dry_run and moves:
        save_undo_log(working_dir, moves)


def save_undo_log(working_dir, moves):
    log_file = working_dir / ".undo_log"
    with open(log_file, "w") as f:
        json.dump(moves, f, indent=2)
    print(f"\nUndo log saved to: {log_file}")


def undo(working_dir):
    log_file = working_dir / ".undo_log"

    if not log_file.exists():
        print("No undo log found")
        return

    with open(log_file, "r") as f:
        moves = json.load(f)

    for move in reversed(moves):
        src = Path(move["to"])
        dest = Path(move["from"])
        src.rename(dest)
        print(f"Restored: {src.name} → {dest.parent.name}/")

    log_file.unlink()
    print("Undo complete")


def main():
    cli_arguments = sys.argv

    if len(cli_arguments) < 2:
        return print("Error: Empty directory argument")

    file_argument = cli_arguments[1]
    working_dir = get_target_directory(file_argument)

    if not working_dir:
        return print("Error: directory not found.")

    if "--undo" in cli_arguments:
        undo(working_dir)
        return

    print(f"Organizing: {working_dir}\n")

    dry_run = "--dry-run" in cli_arguments

    organize_by_extension(working_dir, dry_run=dry_run)



main()
