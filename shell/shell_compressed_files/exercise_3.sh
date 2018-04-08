#!/usr/bin/env bash

bzip2 -z /home/dsc/Data/opentraveldata/optd_por_public.csv 
bzcat /home/dsc/Data/opentraveldata/optd_por_public.csv.bz2 | grep -e '^MAD'

