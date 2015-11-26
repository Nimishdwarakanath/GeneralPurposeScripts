#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script to compute an angle (a dihedral) defined by 3 points (defined by 4 points)
#################################

import math

p1=[0,0,0]
p2=[0,2,0]
p3=[1,3,0]
p4=[1,5,0]

def points2vector(pt1, pt2):
    return [ pt2[0]-pt1[0], pt2[1]-pt1[1], pt2[2]-pt1[2] ]

def mod(v):
    return math.sqrt(v[0]*v[0] + v[1]*v[1] + v[2]*v[2])

def dot(pt1, pt2):
    return pt2[0]*pt1[0] + pt2[1]*pt1[1] + pt2[2]*pt1[2]

def cross(v1, v2):
    return [ v1[1]*v2[2] - v1[2]*v2[1], v1[2]*v2[0] - v1[0]*v2[2], v1[0]*v2[1] - v1[1]*v2[0] ]

def angle(pt1, pt2, pt3):
    v1 = points2vector(pt2, pt1)
    v2 = points2vector(pt2, pt3)
    return math.degrees(math.acos( dot(v1, v2) / (mod(v1)*mod(v2))) )

def dihedral(pt1, pt2, pt3, pt4):
    v1 = points2vector(pt1, pt2)
    v2 = points2vector(pt2, pt3)
    v3 = points2vector(pt3, pt4)
    cross12 = cross(v1, v2)
    cross23 = cross(v2, v3)
    cross1223 = cross(cross12, cross23)
    dot1223 = dot(cross12, cross23)
    mod2 = mod(v2)
    return math.degrees( math.atan2(dot(cross1223, v2) / mod2, dot1223) )

print "Angle between points: ",p1,p2,p3
print angle(p1, p2, p3)
print "Dihedral defined by points: ",p1,p2,p3,p4
print dihedral(p1, p2, p3, p4)
