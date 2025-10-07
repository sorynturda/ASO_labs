#!/bin/bash

PATH=/usr/share/doc/apache2/copyright

grep -E '[a-zA-Z0-9_.]*@[a-zA-Z0-9]*[.][a-zA-Z0-9]*' $PATH
