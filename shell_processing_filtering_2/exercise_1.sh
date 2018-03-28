#!/usr/bin/env bash

cat ~/Data/opentraveldata/optd_aircraft.csv | cut -d '^' -f 3 | grep -E "7[0-9]|3[0-9]{2}"
