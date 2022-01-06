#!/bin/sh
#
# This simple bash script utilizes the swagger-codegen container to generate an
# API-client for python from Contabo's API documentation.
#
local_dir="$(readlink -f $(dirname $0))"

if command -v podman >/dev/null 2>&1; then
  cmd="podman"
else
  cmd="docker"
fi

$cmd run --rm \
  -v "${local_dir}":/local:Z \
  swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://api.contabo.com/api-v1.yaml \
    -l python \
    -o /local/ \
    -c /local/config.json

# Contabo does not declare attributes as nullable, so I have to catch them manually
sed -i 's/^\(\s\+\)self\.\([a-z][a-z_]\+\) = \2$/\1if \2 is not None:\n\1    self.\2 = \2/g' pfruck_contabo/models/*_response{,_data}.py

# No functionality in unit-tests, they just validate that all files have valid syntax :)
python -m unittest
