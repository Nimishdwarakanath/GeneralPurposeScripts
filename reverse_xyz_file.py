#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Purpose: reverse XYZ file
#################################

import sys

# script usage help
if len(sys.argv) != 3:
        sys.exit("Usage : ./this_script XYZ_file number_of_atoms ")

# read HISTORY file
lines = open(sys.argv[1],'r').readlines()

# process file
i = 1
j = 0
while (len(lines) - i * (int(sys.argv[2])+2)) > -1:
        for l in range(len(lines)-i*(int(sys.argv[2])+2),len(lines)-j*(int(sys.argv[2])+2)):
                print lines[l],
        j = i
        i = i + 1
