import sys
from pathlib import Path
from colorama import Fore, Style, init

# Ініціалізація colorama
init(autoreset=True)

def show_directory(path, indent=""):
    for item in sorted(path.iterdir()):
        if item.is_dir():
            print(f"{indent}{Fore.BLUE}📂 {item.name}")
            show_directory(item, indent + "    ")
        else:
            print(f"{indent}{Fore.GREEN}📜 {item.name}")

def main():
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Помилка: вкажіть шлях до директорії")
        print("Використання: python task3.py /шлях/до/директорії")
        sys.exit(1)

    path = Path(sys.argv[1])

    if not path.exists():
        print(f"{Fore.RED}Помилка: шлях не існує: {path}")
        sys.exit(1)

    if not path.is_dir():
        print(f"{Fore.RED}Помилка: це не директорія: {path}")
        sys.exit(1)

    print(f"{Fore.BLUE}📦 {path.name}")
    show_directory(path)

if __name__ == "__main__":
    main()