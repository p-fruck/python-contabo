#!/bin/sh
# Simple script to clean the project directory

proj_dir="$(readlink -f $(dirname $0))/.." # root directory of the project

find "${proj_dir}" -maxdepth 1 ! -name LICENSE ! -name custom ! -name ".git*" ! -name ".*ignore" -exec rm -r {} \;
