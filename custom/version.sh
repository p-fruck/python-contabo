#!/bin/sh

if [ -z "$1"  ]; then
    echo "Usage: $0 <version>"
    echo "  Example: $0 3.2.1"
    exit 1
fi

dir=$(dirname $0)

sed -i "s/^VERSION.*/VERSION = \"$1\"/g" "${dir}/../setup.py"
sed -i -E "s/(\s)\"packageVersion.*/\1\"packageVersion\": \"$1\"/g"  "${dir}/config.json"
"${dir}/build.sh"
