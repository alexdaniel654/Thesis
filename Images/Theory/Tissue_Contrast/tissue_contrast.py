# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 18:26:04 2020

@author: Alex Daniel
"""
import nephtools as nt
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

t = np.linspace(0, 5000, 1000)
t1_cortex = 1376
t1_medulla = 1655

m0 = 1
signal_cortex = nt.T1eq(t, t1_cortex, m0)
signal_medulla = nt.T1eq(t, t1_medulla, m0)
signal_diff = signal_cortex - signal_medulla

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 4.8))
ax1.plot(t, signal_cortex, label='Cortex')
ax1.plot(t, signal_medulla, label='Medulla')
ax1.plot([0, t.max()], [0, 0], 'k', zorder=1)
ylim = ax1.get_ylim()
ax1.vlines(t[np.argmax(signal_diff)], ylim[0], ylim[1], colors='0.5', linestyles='dashed', label='Optimum Contrast')
ax1.set_ylabel('Signal')
ax1.set_yticklabels([])
ax1.set_yticks([-1, -0.5, 0, 0.5, 1])
ax1.set_xlim([0, t.max()])
ax1.set_ylim(ylim)
ax1.legend()

ax2.plot(t, signal_diff, label='Difference')
ylim = ax2.get_ylim()
ax2.vlines(t[np.argmax(signal_diff)], ylim[0], ylim[1], colors='0.5', linestyles='dashed', label='Optimum Contrast')
ax2.set_xlabel('TI ($ms$)')
ax2.set_ylabel('Signal Difference')
ax2.set_yticklabels([])
ax2.set_ylim(ylim)

fig.savefig('tissue_contrast.eps', bbox_inches='tight', dpi=300)