# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 18:35:55 2021

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
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
def pad_with(vector, pad_width, iaxis, kwargs):
    pad_value = kwargs.get('padder', 0)
    vector[:pad_width[0]] = pad_value
    vector[-pad_width[1]:] = pad_value
    
img = nib.load('T1.nii.gz')
data = img.get_fdata()
data = np.rot90(data[:, 132, :])
data_ft = np.fft.fftshift(np.fft.fft2(data))
fig1, (ax11, ax12) = plt.subplots(1, 2, figsize=(6.4, 4.8))
ax11.imshow(np.log(np.abs(data_ft)), cmap='inferno')
kx, ky = [[0, 128], [128, 256]]
ku, kv = [[256, 0], [0, -256]]
ax11.quiver(kx, ky, ku, kv, color="k", scale_units='xy', angles='xy', scale=1)
ax11.text(225, 118, '$k_x$')
ax11.text(132, 25, '$k_y$')
ax11.axis(False)
ax12.imshow(data, cmap='gray')
ax12.axis(False)
fig1.savefig('kspace_full.eps', bbox_inches='tight', dpi=300)

nsamp = 256
width = 256
if nsamp > width:
    nsamp = width
scale = (nsamp/256) * (width/256)
x = np.linspace(128-(width//2), 128+(width//2), nsamp+1)[:-1]
y = np.linspace(128-(width//2), 128+(width//2), nsamp+1)[:-1]
xx, yy = np.meshgrid(x, y)
xx = xx.reshape(-1).astype(int)
yy = yy.reshape(-1).astype(int)
data_ft_rs = data_ft[xx, yy].reshape((nsamp, nsamp))
# data_ft_rs = transform.resize(data_ft_rs, (256, 256))
# data_ft_rs = np.pad(data_ft_rs, 64, pad_with)
data_rs = np.fliplr(np.rot90(np.fft.ifft2(data_ft_rs), 3))

x_plot = np.linspace(128-(width//2), 128+(width//2), (nsamp//8)+1)#[:-1]
y_plot = np.linspace(128-(width//2), 128+(width//2), (nsamp//8)+1)#[:-1]
xx_plot, yy_plot = np.meshgrid(x_plot, y_plot)
xx_plot = xx_plot.reshape(-1).astype(int)
yy_plot = yy_plot.reshape(-1).astype(int)

fig2, (ax21, ax22) = plt.subplots(1, 2, figsize=(6.4, 4.8))
ax21.imshow(np.log(np.abs(data_ft)), cmap='inferno')
ax21.scatter(xx_plot, yy_plot, s=1, marker='x', alpha=0.7, color='C2')
kx, ky = [[0, 128], [128, 0]]
ku, kv = [[256, 0], [0, 256]]
ax21.quiver(kx, ky, ku, kv, color="k", scale_units='xy', angles='xy', scale=1)
ax21.text(225, 138, '$k_x$')
ax21.text(132, 230, '$k_y$')
ax21.axis(False)
ax21.set_xlim((0,255))
ax21.set_ylim((0,255))
ax22.imshow(np.abs(data_rs), cmap='gray')
ax22.axis(False)

fig2.savefig('kspace_full_sample.eps', bbox_inches='tight', dpi=300)

nsamp = 256
width = 64
if nsamp > width:
    nsamp = width
scale = (nsamp/256) * (width/256)
x = np.linspace(128-(width//2), 128+(width//2), nsamp+1)[:-1]
y = np.linspace(128-(width//2), 128+(width//2), nsamp+1)[:-1]
xx, yy = np.meshgrid(x, y)
xx = xx.reshape(-1).astype(int)
yy = yy.reshape(-1).astype(int)
data_ft_rs = data_ft[xx, yy].reshape((nsamp, nsamp))
# data_ft_rs = transform.resize(data_ft_rs, (256, 256))
# data_ft_rs = np.pad(data_ft_rs, 64, pad_with)
data_rs = np.fliplr(np.rot90(np.fft.ifft2(data_ft_rs), 3))

x_plot = np.linspace(128-(width//2), 128+(width//2), (nsamp//8)+1)#[:-1]
y_plot = np.linspace(128-(width//2), 128+(width//2), (nsamp//8)+1)#[:-1]
xx_plot, yy_plot = np.meshgrid(x_plot, y_plot)
xx_plot = xx_plot.reshape(-1).astype(int)
yy_plot = yy_plot.reshape(-1).astype(int)

fig3, (ax31, ax32) = plt.subplots(1, 2, figsize=(6.4, 4.8))
ax31.imshow(np.log(np.abs(data_ft)), cmap='inferno')
ax31.scatter(xx_plot, yy_plot, s=1, marker='x', alpha=0.7, color='C2')
kx, ky = [[0, 128], [128, 0]]
ku, kv = [[256, 0], [0, 256]]
ax31.quiver(kx, ky, ku, kv, color="k", scale_units='xy', angles='xy', scale=1)
ax31.text(225, 138, '$k_x$')
ax31.text(132, 230, '$k_y$')
ax31.axis(False)
ax31.set_xlim((0,255))
ax31.set_ylim((0,255))
ax32.imshow(np.abs(data_rs), cmap='gray')
ax32.axis(False)

fig3.savefig('kspace_centre.eps', bbox_inches='tight', dpi=300)

nsamp = 128
width = 256
if nsamp > width:
    nsamp = width
scale = (nsamp/256) * (width/256)
x = np.linspace(128-(width//2), 128+(width//2), nsamp+1)[:-1]
y = np.linspace(128-(width//2), 128+(width//2), nsamp+1)[:-1]
xx, yy = np.meshgrid(x, y)
xx = xx.reshape(-1).astype(int)
yy = yy.reshape(-1).astype(int)
data_ft_rs = data_ft[xx, yy].reshape((nsamp, nsamp))
# data_ft_rs = transform.resize(data_ft_rs, (256, 256))
# data_ft_rs = np.pad(data_ft_rs, 64, pad_with)
data_rs = np.fliplr(np.rot90(np.fft.ifft2(data_ft_rs), 3))

x_plot = np.linspace(128-(width//2), 128+(width//2), (nsamp//8)+1)#[:-1]
y_plot = np.linspace(128-(width//2), 128+(width//2), (nsamp//8)+1)#[:-1]
xx_plot, yy_plot = np.meshgrid(x_plot, y_plot)
xx_plot = xx_plot.reshape(-1).astype(int)
yy_plot = yy_plot.reshape(-1).astype(int)

fig4, (ax41, ax42) = plt.subplots(1, 2, figsize=(6.4, 4.8))
ax41.imshow(np.log(np.abs(data_ft)), cmap='inferno')
ax41.scatter(xx_plot, yy_plot, s=1, marker='x', alpha=0.7, color='C2')
kx, ky = [[0, 128], [128, 0]]
ku, kv = [[256, 0], [0, 256]]
ax41.quiver(kx, ky, ku, kv, color="k", scale_units='xy', angles='xy', scale=1)
ax41.text(225, 138, '$k_x$')
ax41.text(132, 230, '$k_y$')
ax41.axis(False)
ax41.set_xlim((0,255))
ax41.set_ylim((0,255))
ax42.imshow(np.abs(data_rs), cmap='gray')
ax42.axis(False)

fig4.savefig('kspace_wrap.eps', bbox_inches='tight', dpi=300)
#%%
n_spin = 32
fov = 128
x_plot = np.linspace(0, 255, n_spin)
y_plot = np.linspace(0, 255, n_spin)
xx_plot, yy_plot = np.meshgrid(x_plot, y_plot)
xx_plot = xx_plot.astype(int)
yy_plot = yy_plot.astype(int)
u = np.sin(np.linspace(0, np.pi*4, len(xx_plot)))
v = np.cos(np.linspace(0, np.pi*4, len(xx_plot)))
uu = np.tile(u, (32, 1))
vv = np.tile(v, (32, 1))

outside_thresh = 3
mask_l = np.reshape((data[yy_plot.reshape(-1), xx_plot.reshape(-1)]>outside_thresh) & 
                                     (xx_plot.reshape(-1)<(256 // 2 - fov//2)), (len(x_plot), len(y_plot)))
mask_l = np.logical_or(mask_l, np.roll(mask_l, int(fov*(n_spin/data.shape[0])), 1))

mask_r = np.reshape((data[yy_plot.reshape(-1), xx_plot.reshape(-1)]>outside_thresh) & 
                                     (xx_plot.reshape(-1)>(256 // 2 + fov//2)), (len(x_plot), len(y_plot)))
mask_r = np.logical_or(mask_r, np.roll(mask_r, -int(fov*(n_spin/data.shape[0])), 1))

mask = mask_l + mask_r*2

fig5, ax5 = plt.subplots(figsize=(6.4, 6.4))
ax5.imshow(data, cmap='gray')
ax5.quiver(xx_plot, yy_plot, uu, vv, mask, scale_units='xy', angles='xy', cmap='RdYlGn', scale=0.11)

ax5.axvspan(256 // 2 - fov//2, 256 // 2 + fov//2, alpha=0.3, color='C4', label='FoV')
ax5.axis(False)
ax5.text(128, 245, 'FoV', color='C6', horizontalalignment='center')
fig5.savefig('wrapping_spins.pdf', bbox_inches='tight', dpi=300)