#!/usr/bin/env bash

csvgrep -d '^' -c name -r "^[Aa]ero" /home/dsc/Data/opentraveldata/optd_airlines.csv | csvstat --count
