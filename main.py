from sys import argv
from terminal import Terminal
from tarfile import TarFile
import json

def main():
    #if len(argv) > 1:
    #    config_file = f"{argv[1:]}"
    config_file = "config.json"
    try:
        with open(config_file, "r", encoding="UTF-8") as file:
            data = json.load(file)
            username = data.get("username")
            filesystem_path = data.get("filesystem_path")
            with TarFile(filesystem_path, 'a') as file_system:
                Terminal(username, file_system)
    except FileNotFoundError:
        print(f"Файл {config_file} не найден.")
    #else:
    #    print("Аргументы не были переданы.")

if __name__ == "__main__":
    main()