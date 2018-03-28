#!/usr/bin/env bash

cat ~/Data/opentraveldata/optd_airlines.csv | cut -d '^' -f 8 | grep -c -i -E '^aero'
