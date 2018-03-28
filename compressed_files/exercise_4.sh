#!/usr/bin/env bash

zcat /home/dsc/Data/us_dot/otp/On_Time_On_Time_Performance_2015_1.zip| head -1 | tr ',' '\n' | cat -n | grep -i -E '*carrier*' 
