# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 19:42:08 2019

@author: AnvarVA
"""

# Program to try and work out the power spectrum

import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, fftfreq, ifft

n = 1024
Lx = 100
omg = 2.0*np.pi/Lx

x = [6.145880522, 9.144345513, 12.13847953, 15.13359205, 18.12154072, 21.10676861, 24.08379499, 27.06315455, 30.03333998, 33.00635211, 35.9696599, 38.8925687, 39.49475045, 40.0992139, 40.68758524, 41.28089745, 41.85276341, 42.43272853, 43.04564511, 43.63296098, 44.20280433, 44.75888315, 45.31266982, 45.93764092, 46.50989204, 47.07344788, 47.66551349, 48.26712601, 48.83055172, 49.31317194, 49.90379028, 50.48056564, 51.05668431, 51.6225139, 52.16662394, 52.77442476]


#y1 = 1.0*np.cos( 5.0*omg*x)
#y2 = 1.0*np.sin(10.0*omg*x)
#y3 = 0.5*np.sin(20.0*omg*x)
y = [1.47378E-09, 7.25088E-09, 1.81601E-09, -1.26032E-09, -6.82212E-09, -6.36025E-09, -4.47601E-09, -3.596E-09, -4.53052E-09, -8.44546E-09, -4.48406E-09, -1.65751E-09, 5.08459E-09, 1.35124E-08, 3.31199E-08, 4.99635E-08, 8.10333E-08, 9.77993E-08, 1.57526E-07, 2.13164E-07, 3.07072E-07, 3.97985E-07, 5.37826E-07, 7.01616E-07, 9.37662E-07, 1.22957E-06, 1.5253E-06, 1.9613E-06, 2.40031E-06, 2.90421E-06, 3.57331E-06, 4.43361E-06, 5.44938E-06, 6.38037E-06, 7.48125E-06, 8.69177E-06]
#act = y1 + y2
#yd_true = (omg)*( -5.0*1.0*np.sin(5.0*omg*x) + 10.0*1.0*np.cos(10.0*omg*x) + 20.0*0.5*np.cos(20.0*omg*x))

mean_y = np.mean(y)
std_y = np.std(y)
var_y = std_y**2.0

print(mean_y, std_y, var_y)

# Creates all the necessary frequencies
freqs = fftfreq(n)

# Arranges the frequencies in ascending order
idx = np.argsort(freqs)

# wave numbers
nwaves = freqs*n
nwaves_2pi = omg*nwaves

# mask array to be used for power spectra.
# ignoring half the values, as they are complex conjucates of the other
mask = freqs > 0

# fft values
fft_vals = fft(y)

# Fourier filtering
fft_new = np.copy(fft_vals)
#fft_new[np.abs(nwaves)==20] = 0.0

# inverse fourier transform to reconstruct the filtered data
filt_data = np.real(ifft(fft_new))

# derivative of y in frequency spectrum
#yd_fft = 1.0j*nwaves_2pi*fft_vals
#yd_recon = np.real(ifft(yd_fft))

# this is the power spectra
ps = 2.0*np.abs(fft_vals/n)**2.0

# power by variance
pow_var = ps/var_y*100.0

# freq.power spectra - for variance preserving form
#fps = ps*freqs

#print(fft_vals)
#print(np.abs(fft_vals*2.0/n))
#print(np.sum(ps[mask]))

plt.figure(1)
plt.title('Original Signal')
plt.plot(x, y, color='xkcd:salmon', label='original')
plt.legend()

#plt.figure(2)
#plt.plot(nwaves[mask], ps[mask], label='wavenumber vs spectra')
#plt.title('Power Spectrum Example - wavenumber vs spectra')
#plt.legend()

#plt.figure(3)
#plt.title('Data Filtering example')
#plt.plot(x, act, color='black', label='theoretical')
#plt.plot(x, filt_data, color='cyan', label='via fourier filtering')
#plt.legend()

#plt.figure(4)
#plt.title('Derivative of the signal')
#plt.plot(x, yd_true, color='black', label='theoretical')
#plt.plot(x, yd_recon, color='cyan', label='via spectral method')
plt.legend()
plt.show()