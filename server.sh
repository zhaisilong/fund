#!/usr/bin/env bash

set -e

make clean
make html

pushd build/html
python -m http.server 8000
popd