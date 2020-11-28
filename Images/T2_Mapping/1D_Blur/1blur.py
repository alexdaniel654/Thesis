# -*- coding: utf-8 -*-
"""
Created on Tue Apr 28 11:00:26 2020

@author: Alex Daniel
"""

import os
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import nephtools as nt
import nibabel as nib
import pandas as pd
from nibabel.processing import sigma2fwhm, fwhm2sigma

res = 10000
ran = 10
scale = res//ran #px/mm
x = np.linspace(-ran/2, ran/2, res)
f = np.zeros(res)
ob_size = 0.1
f[int(res//2 - (scale)*ob_size//2):int(res//2 + (scale)*ob_size//2)] = 1
# f = np.linspace(0, 1, res)
# f = np.cos(np.linspace(0,4*np.pi, res))/2 + 0.5

fwhm = 5 #mm
sigma = fwhm2sigma(fwhm*scale)
g = signal.gaussian(res, std=sigma)

plt.plot(x, f, label='$f(x)$')
plt.plot(x, g, label='$g(x)$')
plt.legend()
# plt.savefig('orig.eps')
# plt.show()

F = np.fft.fftshift(np.fft.fft(f))
G = np.fft.fftshift(np.fft.fft(g))

# plt.plot(x, np.abs(F), label='$F(x)$')
# plt.plot(x, np.abs(G), label='$G(x)$')
# plt.legend()
# plt.savefig('fourier.eps')
# plt.show()

H = F * G

# plt.plot(x, np.abs(H), label='$H(x)$', color='C2')
# plt.legend()
# plt.savefig('prod.eps')
# plt.show()

h = np.fft.ifftshift(np.fft.ifft(H))
plt.plot(x, np.abs(h)/np.abs(h).max(), label='$h(x)$')
plt.legend()
# plt.savefig('conv.eps')
plt.show()

