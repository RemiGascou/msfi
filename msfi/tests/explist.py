#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import pexpect
import re

# child = pexpect.spawn("nc localhost 2234")
child = pexpect.spawn("msfconsole")
child.expect("msf5\x1b[0m >", timeout=20)
# print("1(before):",str(child.before))
# print("1(after) :",str(child.after))
print(child.after.decode("ISO-8859-1"))
child.send("\n")
child.expect("msf5 >", timeout=20)
# print("2(before):",str(child.before))
# print("2(after) :",str(child.after))
print(child.after.decode("ISO-8859-1"))
child.expect("msf5", timeout=20)
print("3(before):",str(child.before))
print("3(after) :",str(child.after))
