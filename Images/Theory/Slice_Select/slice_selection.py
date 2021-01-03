# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:26:24 2021

@author: Alex Daniel
"""
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

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1], label='Gradient')
ax.plot([0, 0.2, 0.2], [0.2, 0.2, 0], 'k:')
ax.plot([0, 0.3, 0.3], [0.3, 0.3, 0], 'k:')
ax.plot([0, 0.6, 0.6], [0.6, 0.6, 0], 'k:')
ax.plot([0, 0.8, 0.8], [0.8, 0.8, 0], 'k:')
ax.text(0.01, 0.225, '$\Delta \omega$')
ax.text(0.01, 0.675, '$\Delta \omega$')
ax.text(0.2, -0.06, '$\Delta z$')
ax.text(0.65, -0.06, '$\Delta z$')
ax.text(0.55, 0.92, '$\omega=\gamma G_z z$')
ax.arrow(-0.05, 0.2, 0, 0.1, color='k')
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.set_xlabel('$z$')
ax.set_ylabel('Frequency')
ax.set_aspect('equal', 'box')
fig.savefig('slice_select.eps', bbox_inches='tight', dpi=300)