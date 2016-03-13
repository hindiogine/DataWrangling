#!/home/henk/anaconda3/bin/python
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:45:54 2016

@author: henk
"""

import os

DATADIR  = ""
DATAFILE = "beatles-diskography.csv"

datafile = os.path.join(DATADIR, DATAFILE)

def parse_file(datafile):
#    data = []
    with open(datafile, "r") as f:
        for line in f:
            print(line)

        
parse_file(datafile)