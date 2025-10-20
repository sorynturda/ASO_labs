#!/usr/bin/env python3
import sys
import os


def main(cmd: str):
    paths = [path for path in os.getenv("PATH").split(":")]
    for path in paths:
        programs = os.listdir(path)
        if cmd in programs:
            print(os.path.join(path, cmd))
            return
    print("there is no program called:", cmd)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <program_name>")
    else:
        main(sys.argv[1])
