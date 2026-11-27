import shutil
import time
from pathlib import Path

MINUTES = 15
TIME_WINDOW_SECONDS = MINUTES * 60


def get_recently_modified_files(directory: Path, seconds: int) -> list[Path]:
    now = time.time()
    current_script = Path(__file__).resolve() if "__file__" in globals() else None
    inputTxtFile = Path("inp.txt").resolve()
    recent_files = []

    for item in directory.iterdir():
        if not item.is_file():
            continue
        if current_script and item.resolve() == current_script:
            continue  # Skip the script itself
        if item.resolve() == inputTxtFile:
            continue
        if (now - item.stat().st_mtime) <= seconds:
            recent_files.append(item)

    return recent_files


def main():
    cwd = Path.cwd()
    recent_files = get_recently_modified_files(cwd, TIME_WINDOW_SECONDS)

    if not recent_files:
        print(f"No files modified in the last {MINUTES} minutes in {cwd}")
        return

    print(f"Files modified in the last {MINUTES} minutes:")
    for idx, file_path in enumerate(recent_files, start=1):
        mod_time = time.strftime("%H:%M:%S", time.localtime(file_path.stat().st_mtime))
        print(f"  {idx}. {file_path.name} (modified at {mod_time})")

    choice = input("\nDo you want to move these files to another directory? (y/n): ").strip().lower()
    if choice in ['y','Y','yes','YES','']:
        pass
    else:
        print("Operation cancelled.")
        return

    dest_input = "cses and leetcode"
    if not dest_input:
        print("No path entered. Operation cancelled.")
        return

    dest_dir = Path(dest_input).expanduser().resolve()

    if not dest_dir.exists():
        create = input(f"'{dest_dir}' does not exist. Create it? (y/n): ").strip().lower()
        if create == "y":
            dest_dir.mkdir(parents=True, exist_ok=True)
        else:
            print("Operation cancelled.")
            return

    if not dest_dir.is_dir():
        print(f"Error: '{dest_dir}' is not a directory.")
        return

    for file_path in recent_files:
        try:
            shutil.move(str(file_path), str(dest_dir / file_path.name))
            print(f"Moved: {file_path.name} -> {dest_dir}")
        except Exception as e:
            print(f"Failed to move {file_path.name}: {e}")


if __name__ == "__main__":
    main()