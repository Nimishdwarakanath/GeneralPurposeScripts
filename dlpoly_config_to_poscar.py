#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script to convert a DLPOLY CONFIG file into a VASP POSCAR file
#################################

import sys
from string import atof,atoi

if len(sys.argv) != 5:
    sys.exit("Usage : ./this_script CONFIG mx my mz")

nat = (len(open(sys.argv[1], 'r').readlines()) - 5)/2

hist = open(sys.argv[1], 'r')
mx = atoi(sys.argv[2])
my = atoi(sys.argv[3])
mz = atoi(sys.argv[4])

X = 0.0
Y = 0.0
Z = 0.0

r = 0.0
s = 0.0
t = 0.0

hist.readline()
hist.readline()

a1,a2,a3 = hist.readline().split()
b1,b2,b3 = hist.readline().split()
c1,c2,c3 = hist.readline().split()
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
    l=hist.readline().split()
        x,y,z = hist.readline().split()
        x = atof(x)
        y = atof(y)
        z = atof(z)
    for r in range(0,mx):
        for s in range(0,my):
            for t in range(0,mz):
                X = x + a1 * r + b1 * s + c1 * t
                Y = y + a2 * r + b2 * s + c2 * t
                Z = z + a3 * r + b3 * s + c3 * t
##                print "%2s %14.5f %14.5f %14.5f    T   T   T" % (l[0],X,Y,Z)
                print "%2s %14.5f %14.5f %14.5f " % (l[0],X,Y,Z)

hist.close()
