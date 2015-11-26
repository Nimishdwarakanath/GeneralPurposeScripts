#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script for converting (and duplicating) a VASP POSCAR file or concatenated sequence (DIRECT format)
#              into an XYZ file (Cartesian format)
#################################

from string import *
from sys import *

if len(argv) != 5:
    exit("Usage : ./this_script POSCAR(DIRECT) mx my mz")

poscar = open(argv[1],'r')
mx = atoi(argv[2])
my = atoi(argv[3])
mz = atoi(argv[4])

while 1:
    header = poscar.readline()    # skip header line 1
    if not header: break

    scale = atof(poscar.readline().strip())    # line 2

    # box 3x3 matrix
    a1,b1,c1 = poscar.readline().split()    # line 3
    a2,b2,c2 = poscar.readline().split()    # line 4
    a3,b3,c3 = poscar.readline().split()    # line 5
    a1,b1,c1 = scale*atof(a1), scale*atof(b1), scale*atof(c1)
    a2,b2,c2 = scale*atof(a2), scale*atof(b2), scale*atof(c2)
    a3,b3,c3 = scale*atof(a3), scale*atof(b3), scale*atof(c3)

    # atomic symbols
    labels = []
    line = poscar.readline().strip()    # line 6
    for item in line.split():
        labels.append(item)
    # number of each species
    nums = poscar.readline().strip().split()    # line 7
    # total number of atoms
    num_tot = 0
    for x in nums:
        x = atoi(x)
        num_tot = num_tot + x
    print num_tot * mx * my * mz

    poscar.readline()    # skipe DIRECT line 8

    print "comment"
    # convert fractional into cartesian
    for label in labels:
        j = 0
        while j < atoi(nums[labels.index(label)]):
            xf,yf,zf = poscar.readline().split()        # x y z line
            xf,yf,zf = atof(xf), atof(yf), atof(zf)
            x = a1*xf + b1*yf + c1*zf
            y = a2*xf + b2*yf + c2*zf
            z = a3*xf + b3*yf + c3*zf
            for r in range(0,mx):
                for s in range(0,my):
                    for t in range(0,mz):
                        X = x + a1 * r + b1 * s + c1 * t
                        Y = y + a2 * r + b2 * s + c2 * t
                        Z = z + a3 * r + b3 * s + c3 * t
                        print label, X, Y, Z
            j = j + 1

poscar.close()
