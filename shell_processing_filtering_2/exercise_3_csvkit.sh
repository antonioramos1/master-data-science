#!/usr/bin/env bash

csvcut -d '^' -n /home/dsc/Data/opentraveldata/optd_por_public.csv | csvgrep -H -c 1 -m 'name'
