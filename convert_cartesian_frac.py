#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script for converting an XYZ configuration (or a sequence) in Cartesian format
#              into fractional (or reduced) coordinates
#################################

import math
from math import sin,cos,sqrt,acos,asin
from string import atof, atoi

#basic functions
def theta(vec1,vec2):
    theta = acos((vec1[0]*vec2[0] + vec1[1]*vec2[1] + vec1[2]*vec2[2])/((modulus(vec1))*modulus(vec2)))
    return math.degrees(theta)

#get the mod of vector
def modulus(vec1):
    return float(sqrt(vec1[0]*vec1[0] + vec1[1]*vec1[1] + vec1[2]*vec1[2]))

#open necessary files
if len(sys.argv) != 3:
        sys.exit("Usage : ./this_script XYZ_file vectors_file ")

xyz=open(sys.argv[1],'r')
box=open(sys.argv[2],'r')

frame = 0
while 1:
    # control
    line = box.readline()
    if not line: break

    #lattice vectors
    a1,b1,c1 = line.split()
    a2,b2,c2 = box.readline().split()
    a3,b3,c3 = box.readline().split()
    lata = [ atof(a1), atof(b1), atof(c1)]
    latb = [ atof(a2), atof(b2), atof(c2)]
    latc = [ atof(a3), atof(b3), atof(c3)]

    #lattice parameters
    a = modulus(lata)
    b = modulus(latb)
    c = modulus(latc)
    alpha = theta(latb,latc)
    beta = theta(lata,latc)
    gam = theta(lata,latb)

    print " a b c alpha beta gamma",a,b,c,alpha,beta,gam

    #radians needed for sin, cos
    alpha = math.radians(alpha)
    beta = math.radians(beta)
    gam = math.radians(gam)

    frac = [0,0,0]
    cart = [0,0,0]

    #reqd constants for cart2frac matrix
    sa = sin(alpha)
    sb = sin(beta)
    sg = sin(gam)
    ca = cos(alpha)
    cb = cos(beta)
    cg = cos(gam)

    # v = a*b*c*sqrt(1-ca*ca-cb*cb-cg*cg+ 2*ca*cb*cg)
    v = sqrt(1-ca*ca-cb*cb-cg*cg+ 2*ca*cb*cg)

    # conversion matrix
    ## cart2frac = [ [1/a,0,0], [-cg/(a*sg), (1/(b*sg)), 0], [(ca*cg-cb)/(a*v*sg), ((cb*cg-ca)/(b*v*sg)), sg/(c*v)] ]
    cart2frac = [ [1/a,-cg/(a*sg),(ca*cg-cb)/(a*v*sg)], [0,(1/(b*sg)),((cb*cg-ca)/(b*v*sg))], [0,0,sg/(c*v)] ]

    #get number of atoms
    nat = xyz.readline()
    nat = atoi(nat)
    xyz.readline() # skip comment

    #get cartesian coordinates ... C 1.234 1.234 1.234
    for index in range(nat):
        cart = [ 0,0,0 ]
        lab,x,y,z = xyz.readline().split()
        cart = [atof(x),atof(y),atof(z)]

        #conversion
        frac = [0.0,0.0,0.0]
        for i in range(0,3):
            for j in range(0,3):
                frac[i] = cart2frac[i][j]*cart[j] + frac [i]

        print '%s %14.5f %14.5f %14.5f' % (lab, frac[0], frac[1], frac[2])
    frame = frame + 1

box.close()
xyz.close()
