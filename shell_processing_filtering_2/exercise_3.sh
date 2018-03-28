#!/usr/bin/env bash

head -1 ~/Data/opentraveldata/optd_por_public.csv | tr '^' '\n' | cat -n | grep 'name'
