#!/bin/bash
echo

for corpus in $(cat corpora.txt)
do
  echo "Validating '$corpus'..."
  pkg=$corpus/datapackage.json
  datapackage validate $pkg
  goodtables $pkg
done
