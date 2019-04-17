# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:17:53 2019

@author: AnvarVA
"""

import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

n = 1000

Lx = 100

omg = 2.0*np.pi/Lx

x = np.linspace(0,Lx, n)
y1 = 1.0 * np.cos(19.0*omg*x)
y2 = 1.0 * np.sin(10.0*omg*x)
y3 = 1.0 * np.sin(100.0*omg*x)

y = y1 + y2 + y3

freqs = fftfreq(n)

mask = freqs > 0

fft_vals = fft(y)

fft_theo = 2.0 * np.abs(fft_vals/n)

plt.figure(1)
plt.title('Original signal')
plt.plot(x, y, color = 'xkcd:salmon', label = 'original')
plt.legend()

plt.figure(2)
plt.plot(freqs, fft_vals, label = "raw fft values")
plt.title("Raw FFT values")

plt.show()