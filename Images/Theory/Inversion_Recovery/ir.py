# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 12:51:32 2020

@author: Alex Daniel
"""
import numpy as np
import nephtools as nt
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context('talk')

# matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
t = np.linspace(0, 5000, 100)
t1 = 1000 # ms
s = nt.T1eq(t, t1, 1)

plt.plot([0, t.max()], [0, 0], 'k', zorder=1)
plt.plot(t, s, zorder=3)
plt.xlabel('TI ($ms$)')
plt.ylabel('$M_z(t)$')
plt.xlim([0, t.max()])
plt.grid(True)

plt.savefig('ir.eps', bbox_inches='tight', dpi=300)