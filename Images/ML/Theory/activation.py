# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:35:15 2021
@author: Alex Daniel
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
sns.set_context('talk')

def relu(x):
    return np.maximum(x, 0)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

x = np.linspace(-5, 5, 100)

fig1, ax1 = plt.subplots()
ax1.plot(x, relu(x))
ax1.plot([-5, 5], [0, 0], zorder=1, color='0')
ax1.plot([0, 0], [0, 5], zorder=3, color='0')
ax1.spines['left'].set_position('zero')
ax1.set_xlim([-5, 5])
ax1.set_ylim([-0.05, 5])
fig1.savefig('relu.pdf', dpi=300, bbox_inches='tight')


fig2, ax2 = plt.subplots()
ax2.plot(x, sigmoid(x))
ax2.plot([-5, 5], [0, 0], zorder=1, color='0')
ax2.plot([0, 0], [0, 5], zorder=3, color='0')
ax2.spines['left'].set_position('zero')
ax2.set_xlim([-5, 5])
ax2.set_ylim([-0.01, 1])
fig2.savefig('sigmoid.pdf', dpi=300, bbox_inches='tight')