#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script to add a Gaussian broadening to a spectrum of single values
#              (e.g. vibrational intensities in function of frequencies)
#################################

from sys import *
from math import *
from string import atof, atoi

def frange(iv,fv,jump):
    while iv < fv:
        yield iv
        iv = iv + jump
#   G(mean, height/standard deviation, x, width factor)
def G(mu,h,x,width):
    sigma = 1./(h * sqrt(2.*pi))
    return (1./(sigma * sqrt(2.*pi))) * exp((-1./2.)*((x-mu)/(width*sigma))**2)

if len(argv) != 5:
    exit("Usage : ./add_gaussian.py  [data_file]  [frequency_start]  [frequency_end]  [width_factor]\ndata file: freqency intensity")

start = atof(argv[2])
end = atof(argv[3])
factor = atof(argv[4])

file = open(argv[1],'r')
X = []
Y = []
for x in frange(start, end, 0.02):
    X.append(x)
    Y.append(0.0)

while True:
    line = file.readline()
    if not line: break

    freq,intensity = line.split()
    freq = atof(freq)
    intensity = atof(intensity)

    for x,y in zip(frange(start, end, 0.02), range(len(X))):
        Y[y] = Y[y] + (G(freq, intensity, x, factor))
for x,y in zip(X,Y):
    print x,y
