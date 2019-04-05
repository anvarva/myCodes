# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:10:33 2019

@author: AnvarVA

All the equations are in the link 
    http://bilimneguzellan.net/fuyye-serisi/
"""
from python2matlab_funcs import *


#def integrand_sin(x, m, n):
#    return sin(n*x)*sin(m*x)
#
#
#def a_0(f_x):
#    return (1/pi)*quad(f_x, -pi, pi)[0]
#
#def a_n(f_x):
#    return (1/pi)*quad(f_x*cos(n*x), -pi, pi, args=(n))[0]
#
#def b_n(f_x):
#    return (1/pi)*quad(f_x*sin(n*x), -pi, pi, args=(n))[0]
#
#   
#
#n = 20
#m = 20
#
#I_sin = (1/pi) * quad(integrand_sin, -pi, pi, args=(m,n))[0]



f_x = 0
t = linspace(0,4,0.01)

L = 1 # half of the period
n = 3 # number of harmonics

for ni in linspace(1,n+1,2):
    f_x = f_x + (4/((ni)*pi)*sin((ni)*pi*t/L))
    print(ni)

plot(t,f_x,label = 'sin')
show()

#fig, ax = subplots()
#subplots_adjust(left=0.25, bottom=0.25)



