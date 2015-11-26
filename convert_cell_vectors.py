#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script for converting cell vectors (in Cartesian)
#              into cell parameters and angles (crystallographic).
#################################

import math
from math import sin,cos,sqrt,acos,asin
from string import atof

# get angle between two vectors
def theta(vec1,vec2):
    theta = acos((vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2])/((modulus(vec1))*modulus(vec2)))
    #print math.degrees(theta)
    return math.degrees(theta)

# get the mod of vector
def modulus(vec1):
    return float(sqrt(vec1[0]*vec1[0] + vec1[1]*vec1[1] + vec1[2]*vec1[2]))

if len(sys.argv) != 2:
        sys.exit("Usage : ./this_script cell_vectors_file ")

box=open(sys.argv[1],'r')

while True:
    testline = box.readline()
    if not testline:
        break

    a,b,c = testline.split()
    a=atof(a)
    b=atof(b)
    c=atof(c)
    lata = [ a , b , c ]

    a,b,c = box.readline().split()
    a=atof(a)
    b=atof(b)
    c=atof(c)
    latb = [ a , b , c ]

    a,b,c = box.readline().split()
    a=atof(a)
    b=atof(b)
    c=atof(c)
    latc = [ a , b , c ]

    a = modulus(lata)
    b = modulus(latb)
    c = modulus(latc)
    alpha = theta(latb,latc)
    beta = theta(lata,latc)
    gam = theta(lata,latb)

    # radians needed for sin, cos
    alphar = math.radians(alpha)
    betar = math.radians(beta)
    gamr = math.radians(gam)
    # constants for cart2frac matrix
    sa = sin(alphar)
    sb = sin(betar)
    sg = sin(gamr)
    ca = cos(alphar)
    cb = cos(betar)
    cg = cos(gamr)

    # cell volume
    v = a * b * c * sqrt(1 - ca*ca - cb*cb - cg*cg + 2*ca*cb*cg)

    print "a, b, c: ",a,b,c
    print "alpha, beta, gamma: ",alpha,beta,gam
    print "volume: ",v

box.close()
