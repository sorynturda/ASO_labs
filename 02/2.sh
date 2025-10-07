#!/bin/bash

if [[ $# -ne 1 ]]; then
    echo "$0 <file_path>"
    exit 1
fi

grep -c -E [.]* $1
