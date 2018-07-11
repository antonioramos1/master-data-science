#!/usr/bin/env bash

cat /home/dsc/Data/opentraveldata/optd_aircraft.csv| csvgrep -d '^' -c 'manufacturer' -m 'Airbus' | csvformat -D "|" >> airbus.csv

