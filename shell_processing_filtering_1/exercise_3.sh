#!/usr/bin/env bash

head -n +1 /home/dsc/Data/opentraveldata/optd_por_public.csv | tr '^' '\n' | wc -l
