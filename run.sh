#!/bin/bash

file="sd-ufcg.cfg"
if [ -f "$file" ]
then
    export PYTHONPATH=":"`pwd`
    python app.py
else
	echo "Could not find $file in current directory, please create the $file file"
fi