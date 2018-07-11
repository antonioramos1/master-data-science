#!/usr/bin/env bash

find /home/dsc/Data -maxdepth 1 -mindepth 1 -type d -exec sh -c "ls -lS {} | head -4" \;
