#!/usr/bin/env bash

cat /home/dsc/Data/opentraveldata/optd_aircraft.csv | csvcut -d '^' -c manufacturer | csvstat --freq
cat /home/dsc/Data/opentraveldata/optd_aircraft.csv | csvcut -d '^' -c manufacturer | sort | uniq -c | sort -n -r | head -5
