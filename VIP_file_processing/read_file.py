# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 2019

@author: AnvarVA

"""
from python2matlab_funcs import *
from matplotlib.widgets import Slider



t = linspace(0,4,0.02)

L = 1 # half of the period
n = 1 # number of harmonics
f_x = 0
for ni in linspace(1,n+1,2):
    f_x = f_x + (4/((ni)*pi)*sin((ni)*pi*t/L))
    print(ni)




fig, ax = subplots()
subplots_adjust(left=0.25, bottom=0.25)

wave_plot, = plot(t,f_x,lw = 2, color = 'red')
 
axcolor = 'lightgoldenrodyellow'
axes_n = axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
s_n = Slider(axes_n, 'n', 1, 100, valinit=1, valstep = 1)

def update(val):
    n_val = s_n.val
    f_x = 0
    for ni in linspace(1,n_val+1,2):
        f_x = f_x + (4/((ni)*pi)*sin((ni)*pi*t/L))
    wave_plot.set_ydata(f_x)
    fig.canvas.draw_idle()
    
s_n.on_changed(update)
show()

