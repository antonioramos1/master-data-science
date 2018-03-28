#!/usr/bin/env bash

cat /home/dsc/Data/opentraveldata/optd_aircraft.csv | csvcut -d '^' -c manufacturer | csvstat --unique
