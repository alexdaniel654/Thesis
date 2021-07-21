# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 17:00:18 2021

@author: Alex Daniel
"""
import nibabel as nib
import numpy as np
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

img = nib.load('T2_Star.PAR', scaling='fp', strict_sort=True)
data = img.get_fdata()
data = np.fliplr(np.rot90(data, 3))

fig1, ax1 = plt.subplots(figsize=(4, 3))
im1 = ax1.imshow(data[:,:,0,2], cmap='gray', clim=(0, 25000))
cb1 = fig1.colorbar(im1, ax=ax1, label='Magnitude')
ax1.axis(False)
fig1.tight_layout()
fig1.savefig('mag.pdf', bbox_inches='tight', dpi=300)

fig2, ax2 = plt.subplots(figsize=(4, 3))
im2 = ax2.imshow(data[:,:,0,14], cmap='bwr', clim=(-np.pi, np.pi))
cb2 = fig2.colorbar(im2, ax=ax2, label='Phase')
cb2.set_ticks([-np.pi, 0, np.pi])
cb2.set_ticklabels(['$-\pi$', '0', '$\pi$'])
ax2.axis(False)
fig2.tight_layout()
fig2.savefig('phase.pdf', bbox_inches='tight', dpi=300)


