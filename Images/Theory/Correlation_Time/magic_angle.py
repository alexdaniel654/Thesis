# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 12:51:54 2021
@author: Alex Daniel
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
# import seaborn as sns
# sns.set()
# sns.set_context('talk')
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
fov = 6
x = np.linspace(-fov, fov, 2500)
y = np.linspace(-fov, fov, 2500)
mu = 1
x_grid, y_grid = np.meshgrid(x, y)
r_grid = np.sqrt(x_grid**2 + y_grid**2)
theta_grid = np.arctan(x_grid/y_grid)

bz = (mu/(r_grid**3)) * ((3 * np.cos(theta_grid)**2) - 1)
bz[np.abs(bz)<0.00] = 0

fig, ax = plt.subplots()
ax.imshow(bz, clim=(-0.1, 0.1), cmap='bwr')
ax.add_patch(matplotlib.patches.Circle((1250, 1250), 50, fc='C1', ec='k'))
ax.annotate('$\mu$', (1250, 1000), (1250, 1500), ha='center', va='center', arrowprops=dict(arrowstyle='fancy', shrinkA=1, shrinkB=1, fc='C1', ec='k'))
ax.axis(False)
fig.savefig('magic_angle.pdf', trasparent=True, dpi=600, bbox_inches='tight')