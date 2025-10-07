#!/bin/bash

if [[ $# -ne 2 ]];then
    echo "Wrong number of args"
    exit 1
fi

if [[ ! -f $1 ]];then
    echo "First arg must be a file"
    exit 1
fi

echo "1........"
cat $1 | grep -c $2
echo "2........"
cat $1 | grep -c -E "^$2"
echo "3........"
cat $1 | grep -c -E "$2$"
echo "4........"
cat $1 | grep -c -E "[5-9]{3}\s$2"
