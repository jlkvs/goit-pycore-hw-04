import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(directory, prefix=""):
    try:
        entries = sorted(Path(directory).iterdir(), key=lambda e: e.is_file())
    except FileNotFoundError:
        print(Fore.RED + "Error: Directory not found.")
        return
    except NotADirectoryError:
        print(Fore.RED + "Error: The provided path is not a directory.")
        return
    except PermissionError:
        print(Fore.RED + "Error: Permission denied.")
        return
    
    for entry in entries:
        if entry.is_dir():
            print(prefix + Fore.BLUE + Style.BRIGHT + entry.name)
            print_directory_structure(entry, prefix + "    ")
        else:
            print(prefix + Fore.GREEN + entry.name)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python task_three.py <directory_path>")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    print_directory_structure(directory_path)


