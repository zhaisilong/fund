#!/usr/bin/env bash

set -e
pandoc README.rst -o README.md
git add -A && git commit -m "$1"
git push