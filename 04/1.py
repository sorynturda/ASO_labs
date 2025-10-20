#!/usr/bin/env python3
import sys
import os


def main(dir_path: str):
    size, file_ = 0, ""
    for root, dirs, files in os.walk(dir_path):
        for filename in files:
            full_path = os.path.join(root, filename)
            f_size = os.stat(full_path).st_size
            if size < f_size:
                size, file_ = f_size, full_path
#            print(full_path)
    print(file_, size)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"usage: {sys.argv[0]} <dir_path>")
    else:
        main(sys.argv[1])
