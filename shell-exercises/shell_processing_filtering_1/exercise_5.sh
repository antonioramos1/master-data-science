#!/usr/bin/env bash

sort -t '^' -k 14 -n -r /home/dsc/Data/opentraveldata/optd_airlines.csv | head -n +1
