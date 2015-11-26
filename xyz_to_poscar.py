#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script for converting a configuration (Cartesian XYZ) into a VASP POSCAR file (DIRECT format)
#################################

from string import *
from sys import *
from math import *

if len(argv) != 2:
    exit("Usage : ./convert_xyz2poscar.py XYZ_file")

def theta(vec1,vec2):
        theta = acos((vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2])/((modulus(vec1))*modulus(vec2)))
        return math.degrees(theta)

def modulus(vec1):
        return float(sqrt(vec1[0]*vec1[0] + vec1[1]*vec1[1] + vec1[2]*vec1[2]))

xyz = open(argv[1],'r')

nat = xyz.readline()
nat = atoi(nat)

tag,a,b,c,alpha,beta,gamma = xyz.readline().split()
a = atof(a)
b = atof(b)
c = atof(c)
alpha = atof(alpha)
beta = atof(beta)
gamma = atof(gamma)

alphar = radians(alpha)
betar = radians(beta)
gammar = radians(gamma)

sa=sin(alphar)
sb=sin(betar)
sg=sin(gammar)
ca=cos(alphar)
cb=cos(betar)
cg=cos(gammar)

lata = [ a, 0.0, 0.0]
latb = [ b*cg, b*sg, 0.0]
latc = [ c*cb, c*(ca-cb*cg)/sg, c*sqrt(1-(ca**2+cb**2-2*ca*cg)) / sg]

v = sqrt(1-ca*ca-cb*cb-cg*cg+ 2*ca*cb*cg)

cart2frac = [ [1/a,-cg/(a*sg),(ca*cg-cb)/(a*v*sg)], [0,(1/(b*sg)),((cb*cg-ca)/(b*v*sg))], [0,0,sg/(c*v)] ]

print tag
print "1.0"
print lata[0], lata[1], lata[2]
print latb[0], latb[1], latb[2]
print latc[0], latc[1], latc[2]

labels=[]
nums=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
X=[]
Y=[]
Z=[]

for index in range(nat):
    lab,x,y,z = xyz.readline().split()
    x = atof(x)
    y = atof(y)
    z = atof(z)
    if lab not in labels:
        labels.append(lab)
    nums[labels.index(lab)] = nums[labels.index(lab)] + 1

    cart = [ x, y, z ]
    frac = [ 0.0, 0.0, 0.0 ]
    for i in range(0,3):
        for j in range(0,3):
            frac[i] = cart2frac[i][j]*cart[j] + frac[i]
    X.append(frac[0])
    Y.append(frac[1])
    Z.append(frac[2])

for item in labels:
    print item,
print ""
for item in labels:
    print nums[labels.index(item)],
print ""
print "Direct"

for index in range(nat):
    print '%14.5f %14.5f %14.5f' % (X[index], Y[index], Z[index])

xyz.close()
