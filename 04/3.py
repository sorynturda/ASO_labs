#!/usr/bin/env python3
import sys
import os
from shutil import copytree

def empty_dir(dir_path: str) -> bool:
    return os.path.isdir(dir_path) and not os.listdir(dir_path)

def main(dir_path: str):
    dest = os.getcwd() + "/copy"
    yes = input(f"copy {dir_path} to {dest}?:\n'yes' or 'no'\n") == "yes"
    if not yes:
        return
    copytree(dir_path, dest)
    for (root, dirs, filenames) in os.walk(dest):
        for dir in dirs:
            dirs_path = os.path.join(root, dir)
            if empty_dir(dirs_path):
                yes = input(f"do you want to remove {dirs_path} directory?: ") == "yes"
                if yes:
                    os.rmdir(dirs_path)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <dir_path>")
    elif not os.path.isdir(sys.argv[1]):
        print(f"{sys.argv[1]} is not a directory")
    else:
        main(sys.argv[1])
