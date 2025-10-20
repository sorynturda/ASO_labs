#!/usr/bin/env python3
from subprocess import run
import sys
import os


def main(dir_path: str):
    p = run(["/bin/ls", "-a", dir_path], capture_output=True).stdout.decode()
    res = [file for file in p.split()]
    print("listing files using '/bin/ls':", sorted(res))
    print("listing files using 'os.listdir()':", sorted(os.listdir(dir_path))) # shows hidden files and folders

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <dir_path>")
    else:
        main(sys.argv[1])
