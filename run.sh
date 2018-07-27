#!/bin/bash

file="load_balancer.cfg"
if [ -f "$file" ]
then
    export PYTHONPATH=":"`pwd`
    python loadbalancer/cli/main.py
else
	echo "Could not find $file in current directory, please create the $file file"
fi