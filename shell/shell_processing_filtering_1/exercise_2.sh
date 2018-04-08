#!/usr/bin/env bash

cat /home/dsc/Data/opentraveldata/optd_por_public.csv | tr '\n' '|' | tr ' ' '\n' | sort -r | uniq -c | tail -1

