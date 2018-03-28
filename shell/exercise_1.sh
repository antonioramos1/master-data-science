#!/usr/bin/zsh

FILE_NAME="$1"
csvcut -d '^' -c 7 /home/dsc/Data/opentraveldata/$FILE_NAME | csvstat --max
