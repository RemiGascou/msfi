#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import pexpect
import re

coloredtext = """
Mea culpa
msf5 >
Lorem ipsum dolor sit amet sunt in culpa qui officia deserunt mollit anim id est laborum.
\x1b[4mmsf5\x1b[0m test(\x1b[91mLalla\x1b[0m) >\x1b[0m
Deserunt ipsum laborum sit amet sunt in culpa qui deserunt mollit anim id est .
"""

matched = re.findall(r'[\x1b]\[4mmsf5[\x1b]\[0m [a-zA-Z0-9]*\([\x1b]\[91m[a-zA-Z0-9_\/\-]*[\x1b]\[0m\) >', coloredtext)

print("[LOG] Matched %d lines :"%len(matched))
for line in matched:
    print(line)
