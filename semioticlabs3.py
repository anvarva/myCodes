
# coding: utf-8

# In[3]:


from __future__ import division
import numpy as np
import pywt
import math
import pylab
from obspy.core import read
import matplotlib.pyplot as plt
from obspy.signal.tf_misfit import cwt


# Load vibration data for normal and faulty bearings

healthy_data = np.load('C:/Users/AhmadW1/Dropbox/Semiotic Labs/healthy.npy')
faulty_data = np.load('C:/Users/AhmadW1/Dropbox/Semiotic Labs/bb_data.npy')

# Signal paramters
fs = int(22050.0)                                       # sampling rate
uplim_t = 0.1
t = np.linspace(0, uplim_t, uplim_t * fs)              # time vector
dt = t[1] - t[0]
fmin = 500
fmax = 10000
scale = 12


xhealthy = healthy_data[0:int(uplim_t*fs), 1]       # vibration signal from healthy bearings
xfaulty = faulty_data[0:int(uplim_t*fs), 1]         # vibration signal from faulty bearings


# Extract average feature from signal

def get_ave_values(xvalues, yvalues, n = 3):
    signal_length = len(xvalues)
    if signal_length % n == 0:
        padding_length = 0
    else:
        padding_length = n - signal_length//n % n
    xarr = np.array(xvalues)
    yarr = np.array(yvalues)
    xarr.resize(signal_length//n, n)
    yarr.resize(signal_length//n, n)
    xarr_reshaped = xarr.reshape((-1,n))
    yarr_reshaped = yarr.reshape((-1,n))
    x_ave = xarr_reshaped[:,0]
    y_ave = np.nanmean(yarr_reshaped, axis=1)
    return x_ave, y_ave


# Fast fourier transform

def plot_fourier(t, data, fs, title):
    
    t, data = get_ave_values(t, data)
    n = len(data)                 # length of the signal
    k = np.arange(n)
    T = n/fs
    frq = k/T                    # two sides frequency range
    frq = frq[range(int(n/2))]   # one side frequency range
    Y = np.fft.fft(data)/n       # fft computing and normalization
    Y = Y[range(int(n/2))]
    
    fig, ax = plt.subplots(figsize=(15, 6))
    ax.plot(frq, abs(Y), 'b', label='signal')
    ax.set_title('Fourier transform_' + title, fontsize=18)
    ax.set_xlabel('Freq (Hz)')
    ax.set_ylabel('|Y(freq)|')
    ax.set_ylim([0, 50000])
    ax.legend()

    
# Wavelet transfom of vibration signal

def plot_wavelet(t, data, dt, scale, fmin, fmax, title):
    
    t, data = get_ave_values(t, data)
    scalogram = cwt(data, dt, scale, fmin, fmax, wl='morlet')

    fig = plt.figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
    ax1 = fig.add_axes([0.1, 0.1, 0.7, 0.60])
    ax2 = fig.add_axes([0.1, 0.75, 0.75, 0.2])
    ax3 = fig.add_axes([0.83, 0.1, 0.03, 0.6])
    img = ax1.imshow(np.abs(scalogram), extent=[t[0], t[-1], fmin, fmax], 
              aspect='auto', interpolation="nearest")

    ax1.set_title('Wavelet spectrum_' + title)
    ax1.set_xlabel("Time (sec)") 
    ax1.set_ylabel("Frequency [Hz]")
    ax1.set_yscale('linear')
    ax2.set_title('Vibration signal (Time averaged)_' + title)
    ax2.plot(t, data, 'k')
    ax2.set_ylabel('Amplitude')

    fig.colorbar(img, cax=ax3).set_label('Intensity')
    plt.show()


plot_fourier(t, xhealthy, fs, title='Healthy bearings')
plot_fourier(t, xfaulty, fs, title='Faulty bearings')
    
plot_wavelet(t, xhealthy, dt, scale, fmin, fmax, title='Healthy bearings')
plot_wavelet(t, xfaulty, dt, scale, fmin, fmax, title='Faulty bearings')

