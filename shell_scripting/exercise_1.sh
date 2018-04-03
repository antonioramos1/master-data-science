#!/usr/bin/env bash

FILE_NAME="$1"

csvsort -d '^' -r -c 7 /home/dsc/Data/opentraveldata/$FILE_NAME | csvgrep -c 7 -r "\S" | csvcut -c 3 | head -2 | tail -1

