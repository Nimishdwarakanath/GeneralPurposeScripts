#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script for duplicating an XYZ configuration (or a sequence) in Cartesian format
#              along one (ore more) directions (x,y,z, or a combination)
#################################

import sys
from string import atof,atoi

if len(sys.argv) != 6:
    sys.exit("Usage : ./this_script XYZ_file vectors_file mx my mz")

hist = open(sys.argv[1], 'r')
nat = hist.readline().split()[0]
nat = atoi(nat)
hist.close()

hist = open(sys.argv[1], 'r')
box = open(sys.argv[2], 'r')
mx = atoi(sys.argv[3])
my = atoi(sys.argv[4])
mz = atoi(sys.argv[5])

while 1:

    X = 0.0
    Y = 0.0
    Z = 0.0

    r = 0.0
    s = 0.0
    t = 0.0

    line=hist.readline()
    if not line: break
    hist.readline()

    a1,b1,c1 = box.readline().split()
    a2,b2,c2 = box.readline().split()
    a3,b3,c3 = box.readline().split()
    a1 = atof(a1)
    a2 = atof(a2)
    a3 = atof(a3)
    b1 = atof(b1)
    b2 = atof(b2)
    b3 = atof(b3)
    c1 = atof(c1)
    c2 = atof(c2)
    c3 = atof(c3)

    print nat * mx * my * mz
    print "xyz converted from vesta config"
    for j in range(nat):
            l,x,y,z = hist.readline().split()
            x = atof(x)
            y = atof(y)
            z = atof(z)
        for r in range(0,mx):
            for s in range(0,my):
                for t in range(0,mz):
                    X = x + a1 * r + a2 * s + a3 * t
                    Y = y + b1 * r + b2 * s + b3 * t
                    Z = z + c1 * r + c2 * s + c3 * t
    ##                print "%2s %14.5f %14.5f %14.5f    T   T   T" % (l[0],X,Y,Z)
                    print "%2s %14.5f %14.5f %14.5f " % (l,X,Y,Z)

hist.close()
box.close()
