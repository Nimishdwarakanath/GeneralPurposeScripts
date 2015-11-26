#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script for converting crystallographic cell parameters (a,b,c,alpha,beta,gamma)
#              into cell vectors (in Cartesian)
#################################

import math, sys
from math import sin,cos,sqrt,acos,asin
from string import atof

if len(sys.argv) != 2:
        sys.exit("Usage : ./this_script abc_file ")

abc=open(sys.argv[1],'r')

nil = 0.0

while 1:
	line = abc.readline()
	if not line: break
	a,b,c,alpha,beta,gamma = line.split()
	a = atof(a)
	b = atof(b)
	c = atof(c)
	alpha = atof(alpha)
	beta = atof(beta)
	gamma = atof(gamma)

	alphar = math.radians(alpha)
	betar = math.radians(beta)
	gammar = math.radians(gamma)

	sa=math.sin(alphar)
	sb=math.sin(betar)
	sg=math.sin(gammar)
	ca=math.cos(alphar)
	cb=math.cos(betar)
	cg=math.cos(gammar)

        volume = sqrt( 1 - ca*ca - cb*cb - cg*cg + 2*ca*cb*cg )

	print "%10.8f %10.8f %10.8f" % (a, nil, nil)
	print "%10.8f %10.8f %10.8f" % (b*cg, b*sg, nil)
	print "%10.8f %10.8f %10.8f" % (c*cb, c*((ca - cb*cg)/sg) / sg, c * volume / sg)

abc.close()
