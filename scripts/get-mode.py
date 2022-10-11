#!/usr/bin/python

import sys
import re

if len(sys.argv) != 2: sys.exit(1)

title = sys.argv[1]
mode = "txt-to-img"
prompt = None
match = re.search("^(\[(\w+)\])?\s*(\w[\w\s]*)$", title)
if match.group(2) != None: mode = match.group(2)
if match.group(3) != None: prompt = match.group(3)

if prompt == None or mode == None:
    sys.exit(1)

print(mode)