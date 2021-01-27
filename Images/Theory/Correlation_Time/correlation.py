# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:08:45 2021
@author: Alex Daniel
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
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

b0 = 3
gamma = 42.58E6
omega = gamma * b0
# omega = 400E6
# b0 = omega/gamma
hbar = 6.63E-34/(np.pi * 2)
r = 1.3E-8
tc = np.logspace(-12, -5, 100)

t1 = 1 / ((6 / 20) * ((hbar**2 * gamma **4) / r ** 6) * ((tc / (1 + omega ** 2 * tc ** 2)) + ((4 * tc) / (1 + 4 * omega ** 2 * tc ** 2))))
t2 = 1 / ((3 / 20) * ((hbar**2 * gamma **4) / r ** 6) * (3 * tc + ((5 * tc) / (1 + omega ** 2 * tc ** 2)) + ((2 * tc) / (1 + 4 * omega ** 2 * tc ** 2))))

fig1, ax1 = plt.subplots()
ax1.loglog(tc, t1, label='$T_1$')
ax1.loglog(tc, t2, label='$T_2$')
ax1.axvspan(10E-11, 11E-11, alpha=0.5, color='C2', label='CSF')
ax1.axvspan(10E-9, 11E-9, alpha=0.5, color='C3', label='Muscle')
ax1.axvspan(10E-7, 11E-7, alpha=0.5, color='C4', label='Bone')
ax1.set_xlabel('Correlation Time (s)')
ax1.set_ylabel('Relaxation Time (s)')
# ax1.xaxis.grid(True, which='both')
# ax1.yaxis.grid(True, which='both')

legend_tissue = [Patch(color='C2', alpha=0.5, label='CSF'),
                 Patch(color='C3', alpha=0.5, label='Muscle'), 
                 Patch(color='C4', alpha=0.5, label='Bone')]
legend_relaxation = [Line2D([0], [0], color='C0', label='$T_1$'),
                     Line2D([0], [0], color='C1', label='$T_2$')]
legend_1 = ax1.legend(handles=legend_tissue, loc='lower left', title='Tissue')
ax1.add_artist(legend_1)
ax1.legend(handles=legend_relaxation, loc='right', title='Relaxation')
fig1.savefig('relaxation_correlation.pdf', bbox_inches='tight', dpi=300)

fig2, ax2 = plt.subplots()
b0 = np.linspace(0, 10, 100)
gamma = 42.58E6
omega = gamma * b0
hbar = 6.63E-34/(np.pi * 2)
r = 1.3E-8
tc = np.array([[10E-11, 10E-9, 10E-7]]).T
t1 = 1 / ((6 / 20) * ((hbar**2 * gamma **4) / r ** 6) * ((tc / (1 + omega ** 2 * tc ** 2)) + ((4 * tc) / (1 + 4 * omega ** 2 * tc ** 2))))
t2 = 1 / ((3 / 20) * ((hbar**2 * gamma **4) / r ** 6) * (3 * tc + ((5 * tc) / (1 + omega ** 2 * tc ** 2)) + ((2 * tc) / (1 + 4 * omega ** 2 * tc ** 2))))

ax2.semilogy(b0, t1[0,:], ls=(0, (1.5, 5)), color='C0')
ax2.semilogy(b0, t2[0,:], ls=(2.5, (1.5, 5)), color='C1')
ax2.semilogy(b0, t1[1,:], ls='--', color='C0')
ax2.semilogy(b0, t2[1,:], ls='--', color='C1')
ax2.semilogy(b0, t1[2,:], ls='-', color='C0')
ax2.semilogy(b0, t2[2,:], ls='-', color='C1')
ax2.set_xlabel('$B_0$ (T)')
ax2.set_ylabel('Relaxation Time (s)')

legend_tissue = [Line2D([0], [0], color='0', ls=(0, (1.5, 5)), alpha=1, label='CSF'),
                 Line2D([0], [0], color='0', ls='--', alpha=1, label='Muscle'), 
                 Line2D([0], [0], color='0', ls='-', alpha=1, label='Bone')]
legend_relaxation = [Line2D([0], [0], color='C0', label='$T_1$'),
                     Line2D([0], [0], color='C1', label='$T_2$')]
legend_1 = ax2.legend(handles=legend_tissue, loc='lower right', title='Tissue')
ax2.add_artist(legend_1)
ax2.legend(handles=legend_relaxation, loc='upper right', title='Relaxation')
fig2.savefig('relaxation_b0.pdf', bbox_inches='tight', dpi=300)