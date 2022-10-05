#!/usr/bin/env bash

set -o errexit

PAPERNAME=main

echo cleanning origin files
if [ -e out ]; then
  rm -r out
fi

echo make dir out
mkdir -p out

echo copy files to out ...
ls | grep .tex | xargs -I_ cp _ out/_
ls | grep .bib | xargs -I_ cp _ out/_
ls | grep .cls | xargs -I_ cp _ out/_
cp -r figure out
cp -r image out
cp -r chapters out

echo cd dir out
pushd out

echo compling ...
xelatex $PAPERNAME
biber $PAPERNAME
xelatex $PAPERNAME
xelatex $PAPERNAME
echo get pdf ...
cp *.pdf ..
popd
