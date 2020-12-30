# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 19:29:27 2020

@author: Alex Daniel
"""
import numpy as np
import matplotlib.pyplot as plt

#%% t = 0
spins = 11
spread = 0
origin = np.zeros(spins)
theta = np.linspace(-spread, spread, origin.shape[0])
u = np.cos(theta)
v = np.sin(theta)

theta_full = np.linspace(0, np.pi*2, 100)
fig1, ax1 = plt.subplots()
ax1.quiver(origin, origin, u, v, theta, scale_units='xy', angles='xy', scale=1, cmap='plasma')
ax1.plot(np.cos(theta_full), np.sin(theta_full), 'k')
axlim = 1.2
ax1.set_xlim([-axlim, axlim])
ax1.set_ylim([-axlim, axlim])
ax1.axis(False)
ax1.set_aspect('equal', 'box')

fig1.tight_layout()
fig1.savefig('se_spins_t0.eps', bbox_inches='tight', dpi=300, transparent=True)

#%% t = TE
spins = 11
spread = np.pi/3
origin = np.zeros(spins)
theta = np.linspace(-spread, spread, origin.shape[0])
u = np.cos(theta)
v = np.sin(theta)

theta_full = np.linspace(0, np.pi*2, 100)
fig2, ax2 = plt.subplots()
ax2.quiver(origin, origin, u, v, theta, scale_units='xy', angles='xy', scale=1, cmap='plasma')
ax2.plot(np.cos(theta_full), np.sin(theta_full), 'k')
axlim = 1.2
ax2.set_xlim([-axlim, axlim])
ax2.set_ylim([-axlim, axlim])
ax2.axis(False)
ax2.set_aspect('equal', 'box')

fig2.tight_layout()
fig2.savefig('se_spins_t_te.eps', bbox_inches='tight', dpi=300, transparent=True)

#%% t = TE Post 180
spins = 11
spread = np.pi/3
origin = np.zeros(spins)
theta = np.linspace(-spread, spread, origin.shape[0])
u = np.cos(theta)
v = np.sin(theta)

theta_full = np.linspace(0, np.pi*2, 100)
fig3, ax3 = plt.subplots()
ax3.quiver(origin, origin, u, v, -theta, scale_units='xy', angles='xy', scale=1, cmap='plasma')
ax3.plot(np.cos(theta_full), np.sin(theta_full), 'k')
axlim = 1.2
ax3.set_xlim([-axlim, axlim])
ax3.set_ylim([-axlim, axlim])
ax3.axis(False)
ax3.set_aspect('equal', 'box')

fig3.tight_layout()
fig3.savefig('se_spins_t_te_inverted.eps', bbox_inches='tight', dpi=300, transparent=True)

#%% t = 2TE
spins = 11
spread = np.pi/16
origin = np.zeros(spins)
np.random.shuffle(theta)
u = np.cos(theta)
v = np.sin(theta)
theta = np.linspace(-spread, spread, origin.shape[0])

theta_full = np.linspace(0, np.pi*2, 100)
fig4, ax4 = plt.subplots()
ax4.quiver(origin, origin, u, v, -theta, scale_units='xy', angles='xy', scale=1, cmap='plasma')
ax4.plot(np.cos(theta_full), np.sin(theta_full), 'k')
axlim = 1.2
ax4.set_xlim([-axlim, axlim])
ax4.set_ylim([-axlim, axlim])
ax4.axis(False)
ax4.set_aspect('equal', 'box')

fig4.tight_layout()
fig4.savefig('se_spins_t_2te.eps', bbox_inches='tight', dpi=300, transparent=True)