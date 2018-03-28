#!/usr/bin/env bash

cut -d '^' -f 10 /home/dsc/Data/opentraveldata/optd_airlines.csv | sort | uniq -c
