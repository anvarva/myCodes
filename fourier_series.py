# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 13:10:33 2019

@author: AnvarVA
"""
from python2matlab_funcs import *


#I1 = quad(lambda x: sin(x), -pi, pi)
#I2 = quad(lambda x: sin(x), -pi, pi)[0]



def integrand_sin(x, m, n):
    return sin(n*x)*sin(m*x)
def integrand_cos(x, m, n):
    return cos(n*x)*cos(m*x)
def integrand_sin_cos(x, m, n):
    return sin(n*x)*cos(m*x)
        

n = 20
m = 20

I_sin = (1/pi) * quad(integrand_sin, -pi, pi, args=(m,n))[0]

I_cos = (1/pi) * quad(integrand_cos, -pi, pi, args=(m,n))[0]

I_sin_cos = (1/pi) * quad(integrand_sin_cos, -pi, pi, args=(m,n))[0]

