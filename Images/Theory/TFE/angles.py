# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 19:02:05 2021
@author: Alex Daniel
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import seaborn as sns
sns.set()
sns.set()
sns.set_context('notebook')
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

def sss(alpha, tr, t1):
    return ((np.sin(alpha) * (1 - np.exp(-tr/t1)))/(1 - np.cos(alpha) * np.exp(-tr/t1)))

tr = np.linspace(0, 5000, 250)
alpha = np.linspace(0, np.pi, 250)
# Values for renal cortex from Cox et al 2017
t1 = 1376
t2star = 49.6
tr_grid, alpha_grid = np.meshgrid(tr, alpha)
sig = sss(alpha_grid, tr_grid, t1)
ernst = np.rad2deg(np.arccos(np.exp(-tr/t1)))

df = pd.DataFrame(columns=['tr', 'alpha', 'signal'])
df['tr'] = tr_grid.reshape(-1)
df['alpha'] = alpha_grid.reshape(-1)
df['signal'] = sig.reshape(-1)
df = df.pivot('alpha', 'tr', 'signal')

fig, ax = plt.subplots()
ax = sns.heatmap(df, cbar=False, ax=ax, cmap='inferno', vmin=0, vmax=1)
ax.set_xticks(np.linspace(0, 250, 6))
ax.set_xticklabels(['{:.0f}'.format(x) for x in np.linspace(0, 5000, 6)])
ax.set_xlabel('TR ($ms$)')
ax.set_yticks(np.linspace(0, 250, 5))
ax.set_yticklabels(['{:.0f}'.format(x) for x in np.linspace(0, 180, 5)])
ax.set_ylabel('Flip Angle ($^\circ$)')
cbar = fig.colorbar(plt.imshow(sig, cmap='inferno', clim=(0, 1)))
cbar.ax.set_ylabel('$S_{TFE}$/$M_0$')
ax.plot(np.arange(0.5, 250.5), (ernst/180)*250, label='Ernst Angle', color='C2')
ax.legend(loc='lower left')

fig.savefig('ernst.pdf', bbox_inches='tight', dpi=300)
