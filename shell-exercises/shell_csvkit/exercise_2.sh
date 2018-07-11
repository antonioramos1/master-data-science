#!/usr/bin/env bash

cat /home/dsc/Data/opentraveldata/optd_aircraft.csv | csvcut -d '^' -c manufacturer | csvsort | uniq | tail -n +2 | wc -l
