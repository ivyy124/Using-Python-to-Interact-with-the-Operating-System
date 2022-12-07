#!/usr/bin/env python3

import sys
import subprocess

with open(sys.argv[1], 'r') as file:
  lines = file.readlines()
  for line in lines:
    line = line.strip()
    new_name = line.replace('jane', 'jdoe')
    subprocess.run(["mv", line, new_name])
  file.close()
