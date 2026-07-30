import sys
from pathlib import Path
from colorama import Fore, Back, Style, init

init(autoreset=True)

path = sys.argv[1]

def file_tree(path, prefix=''):

    if not Path(path).exists():
        print(Fore.RED + f"Error: The path '{path}' does not exist.")
        return

    if Path(path).is_file():
        print(Fore.GREEN + prefix + Path(path).name)
        return

    print(Fore.BLUE + prefix + Path(path).name + '/')
    prefix += '    '
    
    for item in sorted(Path(path).iterdir()):
        file_tree(item, prefix)


file_tree(path)