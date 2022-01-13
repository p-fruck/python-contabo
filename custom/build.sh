#!/bin/bash
#
# This simple bash script utilizes the swagger-codegen container to generate an
# API-client for python from Contabo's API documentation.
#
set -e

git_user_id=p-fruck
git_repo_id=python-contabo
proj_dir="$(readlink -f $(dirname $0))/.." # root directory of the project

function customize_readme() {
  mv README.md README.md.gen
  # apply custom introduction to README.md
  cp custom/README.md.part README.md
  # get line number of the requirements heading
  line=$(grep -n '## Getting Started' README.md.gen | cut -d ':' -f 1 | tail -1)
  # add requirements and documentation to README.md
  tail -n+${line} README.md.gen >> README.md
  rm README.md.gen
}

if command -v podman >/dev/null 2>&1; then
  cmd="podman"
else
  cmd="docker"
fi

$cmd run --rm \
  -v "${proj_dir}":/local:Z \
  swaggerapi/swagger-codegen-cli-v3 generate \
    -i https://api.contabo.com/api-v1.yaml \
    -l python \
    --git-user-id ${git_user_id} \
    --git-repo-id ${git_repo_id} \
    -o /local/ \
    -c /local/custom/config.json

cd "${proj_dir}"

# Contabo does not declare attributes as nullable, so I have to catch them manually
sed -i 's/^\(\s\+\)self\.\([a-z][a-z_]\+\) = \2$/\1if \2 is not None:\n\1    self.\2 = \2/g' pfruck_contabo/models/*_response{,_data}.py

# apply custom patches to source files
for patchfile in $(find custom/patches -type f)
do
  patch -p0 < "${patchfile}"
done

# No functionality in unit-tests, they just validate that all files have valid syntax :)
python -m unittest

customize_readme
