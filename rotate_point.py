#!/usr/bin/env python

#################################
# Author: Salah Eddine Boulfelfel
# Date: 11/26/15
# Description: a python script to rotate a point about an axis defined by 2 points (math from Euler Rodrigues method)
#################################

import math

def points2vector(pt1, pt2):
        return [ pt2[0]-pt1[0], pt2[1]-pt1[1], pt2[2]-pt1[2] ]
def dot(pt1, pt2):
        return pt2[0]*pt1[0] + pt2[1]*pt1[1] + pt2[2]*pt1[2]

def rotation_matrix(pt1, pt2, pt3, theta):
        axis = points2vector(pt1, pt2)
        axis = axis[0]/math.sqrt(dot(axis, axis)), axis[1]/math.sqrt(dot(axis, axis)), axis[2]/math.sqrt(dot(axis, axis))
        a = math.cos(theta/2)
        b, c, d = -axis[0]*math.sin(theta/2), -axis[1]*math.sin(theta/2), -axis[2]*math.sin(theta/2)
        aa, bb, cc, dd = a*a, b*b, c*c, d*d
        bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
        return [(aa+bb-cc-dd)*pt3[0]+ 2*(bc+ad)*pt3[1]+ 2*(bd-ac)*pt3[2],
                2*(bc-ad)*pt3[0]+ (aa+cc-bb-dd)*pt3[1]+ 2*(cd+ab)*pt3[2],
                2*(bd+ac)*pt3[0]+ 2*(cd-ab)*pt3[1]+ (aa+dd-bb-cc)*pt3[2]]

# points that define rotation axis
p1=[0,0,0]
p2=[0,0,1]
# coordinates of the point to be rotated
p3=[1.50,1.50,0]
# rotation angle in degrees
alpha=90.0

print "before rotation: ", p3
print "after  rotation: ", rotation_matrix(p1,p2,p3,math.radians(alpha))
