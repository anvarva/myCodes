# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:32:05 2019

@author: AnvarVA
"""

import numpy as np
import scipy.signal as signal
import matplotlib.pyplot as plt

b1 = signal.firwin(40, 0.3)
b2 = signal.firwin(41, [0.3, 0.8])
plt.plot(b1)
plt.plot(b2)
plt.show()

w1, h1 = signal.freqz(b1)
w2, h2 = signal.freqz(b2)

plt.title('Digital filter frequency response')
plt.plot(w1, 20*np.log10(np.abs(h1)), 'b')
plt.plot(w2, 20*np.log10(np.abs(h2)), 'r')
plt.ylabel('Amplitude Response (dB)')
plt.xlabel('Frequency (rad/sample)')
plt.grid()
plt.show()