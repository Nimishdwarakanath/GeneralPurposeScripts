#!/usr/bin/env python

#######################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Purpose: reverse lines of a text file
#######################################

import sys

if len(sys.argv) == 2:
    for i in reversed(open(sys.argv[1], 'r').readlines()):
        print i,
else:
    print "Usage: ./reverse_file.py file_name",
