# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 15:46:15 2021
@author: Alex Daniel
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
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

slew_rate = 200
max_g = 45
rise_time = max_g / slew_rate
grad_on = 1
grad_off = 2
t = np.array([0, grad_on - rise_time, grad_on, grad_off, grad_off + rise_time, 3])
g = np.array([0, 0, max_g, max_g, 0, 0])

ax.plot(t, g, color='C2')

ax.annotate('', xy=(2.25, 0), xytext=(2.25, max_g), arrowprops=dict(arrowstyle='<->', connectionstyle='arc3', color='k'))
ax.text(2.28, max_g/2, 'Peak\ngradient\namplitude', ha='left', va='center')

ax.plot([grad_on - rise_time, grad_on - rise_time], [-5, max_g], ':k')
ax.plot([grad_on, grad_on], [-5, max_g], ':k')
ax.annotate('', xy=(grad_on, -5), xytext=(grad_on - rise_time, -5), arrowprops=dict(arrowstyle='<->', connectionstyle='arc3', color='k'))
ax.text(grad_on - (rise_time/2), -6, 'Rise time', ha='center', va='top')

ax.set_xlim([0, 3])
ax.set_ylim([-10, 50])
ax.set_xlabel('Time (ms)')
ax.set_ylabel('Gradient Amplitude (mT/m)')
fig.savefig('slew.pdf', bbox_inches='tight', dpi=300)