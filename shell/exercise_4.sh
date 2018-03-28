#!/usr/bin/zsh

FILE_NAME="$1"
DELIMITER="$2"
csvcut -d $2 -n /home/dsc/Data/opentraveldata/$FILE_NAME
