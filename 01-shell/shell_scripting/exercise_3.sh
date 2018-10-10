#!/usr/bin/env bash

FILE_NAME="$1"
NUMBER_ENGINES="$2"
csvcut -d '^' -c 7 /home/dsc/Data/opentraveldata/$FILE_NAME | csvgrep -c 1 -m $NUMBER_ENGINES | csvstat --count

