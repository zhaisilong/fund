#!/usr/bin/env bash

set -e

python crawl.py
python analysis.py
python track.py
#python predict.py
