#!/bin/bash
if test $# -ne 2; then
    echo "Wrong number of args"
    exit
fi

if ! test -d $1; then
    echo "First arg must be a directory"
    exit
fi

RES=`find $1 -maxdepth 1 -name $2`

if [[ -z "$RES" ]]; then
    echo "testing text" > "$2.file"
    mkdir -p "$2.dir"
elif [[ -f "$RES" ]]; then
    echo "It is a file"
elif [[ -d "$RES" ]]; then
    echo "It is NOT a file"
else
    echo "Unknown type"
fi
