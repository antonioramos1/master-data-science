#!/usr/bin/env bash

FILE_NAME="$1"
COLUMN_NUMBER="$2"
csvcut -d '^' -c $COLUMN_NUMBER /home/dsc/Data/opentraveldata/$FILE_NAME | csvstat --max
