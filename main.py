#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import msfi

c = msfi.MSFInteract()
c.execute('')

import sys
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage : python3 "+sys.argv[0]+" file")
    else :
        file = sys.argv[1]
