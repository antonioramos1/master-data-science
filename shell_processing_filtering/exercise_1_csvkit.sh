#!/usr/bin/zsh

csvgrep -d '^' -c model -r "7[0-9]7|3[0-9]{2}" /home/dsc/Data/opentraveldata/optd_aircraft.csv | csvcut -c 3 | tail -n +2

