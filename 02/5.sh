#!/bin/bash

if test $# -ne 2; then
    echo "Wrong number of args"
    exit
fi

if ! test -d $1; then
    echo "First arg must be a directory"
    exit
fi

function calculeaza_dimensiune()
{
    RES=$`du -b $1 | cut -f -1`
    return $RES
}

function verifica()
{
    PATH=`find $1 -maxdepth 1 -name $2`
    if [[ -z $PATH ]]; then
        return 1
    else
        return 0
    fi

}

verifica $1 $2
RES=$?
echo $RES

if [[ $RES -eq 0 ]];then
    calculeaza_dimensiune $RES
    echo $?
fi
