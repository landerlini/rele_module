#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 14 11:51:46 2023

@author: passalev
"""

import  ftd2xx as ftd
import time
import sys
releDrv = ftd.open(0)
value1=0x01 #8bit data to output actually only 1st bit active
value0=0x00 #8bit data to output actually only 1st bit active
Mode = 0xff   # Set all line as output
releDrv.setBitMode(Mode, 1)  # bitbang mode and  pin as async output
releDrv.write(chr(value1))# Set output as desired
time.sleep(1)
releDrv.write(chr(value0))      # Set output as desired
time.sleep(1)
releDrv.write(chr(value1))      # Set output as desired
time.sleep(1)
releDrv.write(chr(value0))      # Set output as desired
print(releDrv.read(1))
print(releDrv)
releDrv.close()
