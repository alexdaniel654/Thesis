# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 11:50:42 2021

@author: Alex Daniel
"""
import nibabel as nib
import numpy as np
from skimage import transform
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set()
sns.set_context('talk')
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })
    
img = nib.load('T1.nii.gz')
data = img.get_fdata()
data = np.rot90(data[:, 132, :])
data_ft = np.fft.fftshift(np.fft.fft2(data))

fig1, ax1 = plt.subplots(figsize=(6.4, 6.4))
ax1.imshow(np.log(np.abs(data_ft)), cmap='inferno')
ax1.axis(False)
fig1.savefig('kspace_full.eps', bbox_inches='tight', dpi=300)

data_ift = np.fft.ifft2(data_ft)

fig2, ax2 = plt.subplots(figsize=(6.4, 6.4))
ax2.imshow(np.abs(data_ift), cmap='gray', clim=(0, data.max()))
ax2.axis(False)
fig2.savefig('image_full.eps', bbox_inches='tight', dpi=300)

data_ft_23 = np.copy(data_ft)
data_ft_23[int(data_ft_23.shape[0]*(0.75)):, :] = 0

fig3, ax3 = plt.subplots(figsize=(6.4, 6.4))
ax3.imshow(np.log(np.abs(data_ft_23)), cmap='inferno')
ax3.axis(False)
fig3.savefig('kspace_75.eps', bbox_inches='tight', dpi=300)

data_ift_23 = np.fft.ifft2(data_ft_23)

fig4, ax4 = plt.subplots(figsize=(6.4, 6.4))
ax4.imshow(np.abs(data_ift_23), cmap='gray', clim=(0, data.max()))
ax4.axis(False)
fig4.savefig('image_75.eps', bbox_inches='tight', dpi=300)

data_ft_12 = np.copy(data_ft)
data_ft_12[int(data_ft_23.shape[0]*(0.51)):, :] = 0

fig5, ax5 = plt.subplots(figsize=(6.4, 6.4))
ax5.imshow(np.log(np.abs(data_ft_12)), cmap='inferno')
ax5.axis(False)
fig5.savefig('kspace_51.eps', bbox_inches='tight', dpi=300)

data_ift_12 = np.fft.ifft2(data_ft_12)

fig6, ax6 = plt.subplots(figsize=(6.4, 6.4))
ax6.imshow(np.abs(data_ift_12), cmap='gray', clim=(0, data.max()))
ax6.axis(False)
fig6.savefig('image_51.eps', bbox_inches='tight', dpi=300)