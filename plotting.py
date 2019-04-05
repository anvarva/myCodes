# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:10:33 2019

@author: AnvarVA

All the equations are in the link 
    http://bilimneguzellan.net/fuyye-serisi/
"""


from python2matlab_funcs import *

## function name changing end

theta = linspace(-pi/2,pi/2,0.01)

#Circle radius
r = 1

#Ellispe minor and major axis
tilt_angle = 90 - 20
a = r * (1/cos(tilt_angle*pi/180))
b = r

#circle
x = r*cos(theta)
y = r*sin(theta)

r_circle = sqrt(x**2+y**2)

#ellipse
x1 = a*cos(theta)
y1 = b*sin(theta)

r_ellispe = sqrt(x1**2+y1**2)
#here a>b and theta is in quadrant 1 and 4
#for val in theta
  #  if rem(val,pi/2) = 0:
  #      theta_el = theta
   # else:
theta_el = atan(tan(theta)*b/a)







plot(x,y,label = 'Circle')
plot(x1,y1,label = 'Ellipse')
ylabel('y - axis')
xlabel('x - axis')

show()