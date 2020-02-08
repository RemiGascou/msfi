#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File name          :
# Author             :
# Date created       :
# Date last modified :
# Python Version     : 3.*

import json
import msfi

# Creating MSFInteract object and starting MSF Console
c = msfi.MSFInteract(debug=True)

# Searching for proftpd exploits
results = c.search('proftpd')

# Printing the results in JSON Format
print(json.dumps(results, indent=4))

# Closing MSF Console and MSFInteract
c.close()
