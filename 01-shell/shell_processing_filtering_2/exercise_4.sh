#!/usr/bin/env bash

find /home/ -name "*txt" -exec sh -c "grep -l -i 'science' {}" \; -exec sh -c "grep -i 'science' {}" \;
