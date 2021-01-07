# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 16:06:28 2021
@author: Alex Daniel
"""

import nephtools as nt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
sns.set()
sns.set_context('talk')
# matplotlib.rcParams.update({
#     "pgf.texsystem": "pdflatex",
#     'font.family': 'serif',
#     'text.usetex': True,
#     'pgf.rcfonts': False,
# })
t2 = 500 # ms
t2star = 50 # ms
te = 250 # ms
f0 = 0.8
t_step = 0.1 # ms
t = np.around(np.arange(-5, te * 2, t_step), 1)
t_readout = 35
t_blip = 5

t_sig = t[t>=-0.05]
t2_envelope = nt.T2eq(t_sig, t2, 1)
t2star_envelope_te_by_2 = nt.T2eq(t_sig[t_sig<te], t2star, 1)
t2star_envelope = np.concatenate((np.flip(t2star_envelope_te_by_2), t2star_envelope_te_by_2))
envelope = t2star_envelope * t2_envelope
sig = envelope * np.sin(f0 * t_sig)

fig, axs = plt.subplots(ncols=2, nrows=5, sharex=True, figsize=(14, 7))
gs = axs[0, 1].get_gridspec()
for ax in axs[:, 1]:
    ax.remove()
axk = fig.add_subplot(gs[:, 1])
axrf = axs[0, 0]
axgx = axs[3, 0]
axgy = axs[2, 0]
axgz = axs[1, 0]
axsig= axs[4, 0]

t_rf = np.arange(-50, te *4, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
rf = np.zeros(len(t_rf))
rf[312:688] = sinc * 2
axrf.plot(t_rf/2, rf, 'C1')
axrf.set_yticklabels([])
axrf.set_yticks([-10, 0, 10])
axrf.set_ylim([-0.3, 1.2])
axrf.set_ylabel('RF')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>-13) & (t_grad<13)] = grad_amp
grad[(t_grad>13) & (t_grad<39)] = -grad_amp * 0.5
axgz.plot(t_grad, grad, 'C2')
axgz.set_yticklabels([])
axgz.set_yticks([-1, 0, 1])
axgz.set_ylim([-1.2, 1.2])
axgz.set_ylabel('$G_z$\nSlice')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = -1
blip_amp = 0.2
grad = np.zeros(len(t_grad))
grad[(t_grad>57.5) & (t_grad<92.5)] = grad_amp
for n in np.arange(-5, 4, 1):
    grad[(t_grad>(te-n*t_readout - t_readout/2)-t_blip/2) & (t_grad<(te-n*t_readout - t_readout/2)+t_blip/2)] = blip_amp
gy_cm = matplotlib.cm.plasma
trads = np.linspace(0, 1, 9)
trad_col = [gy_cm(x) for x in trads]
axgy.plot(t_grad, grad, color='C2')
axgy.set_yticklabels([])
axgy.set_yticks([-1, 0, 1])
axgy.set_ylim([-1.2, 1.2])
axgy.set_ylabel('$G_y$\nPhase')

t_grad = np.arange(-50, te *2, t_step)

grad_amp = 1
grad = np.zeros(len(t_grad))
# grad[(t_grad>te-t_readout/2) & (t_grad<te+t_readout/2)] = grad_amp
pol = -1
for n in np.arange(-5, 5, 1):
    grad[(t_grad>(te-n*t_readout)-t_readout/2) & (t_grad<(te-n*t_readout)+t_readout/2)] = pol * grad_amp
    pol *= -1
n=5
grad[(t_grad>(te-n*t_readout)-t_readout/2) & (t_grad<(te-n*t_readout)+t_readout/2)] = pol * grad_amp * 0.5
# grad[(t_grad>75) & (t_grad<175)] = grad_amp
# grad[(t_grad>25) & (t_grad<75)] = -grad_amp
axgx.plot(t_grad, grad, 'C2')
# axgx.plot([7.5, 17.5], [1, 1], 'C3') # Acquisition
axgx.set_yticklabels([])
axgx.set_yticks([-1, 0, 1])
axgx.set_ylim([-1.2, 1.2])
axgx.set_ylabel('$G_x$\nFreq')

axsig.plot(t_sig, sig)
axsig.plot([-50, 0], [0, 0], 'C0')
axsig.axvspan(92.5, 442.4, color='C3', alpha=0.2) #Acquisition
axsig.set_xlabel('Time ($ms$)')
axsig.set_xlim([-50, 500])
axsig.set_yticklabels([])
axsig.set_ylabel('Signal')

kx, ky = [[-1, 0], [0, -1]]
ku, kv = [[2, 0], [0, 2]]
axk.quiver(kx, ky, ku, kv, color="k", scale_units='xy', angles='xy', scale=1)
kys = np.linspace(-1, 1, 9)
trad_col.reverse()
axk.plot([0, -1], [0, -1], 'C3')
for ind, y in enumerate(kys[:-1]):
    side = ((ind % 2) * -2) + 1
    axk.plot([side, side], [y, kys[ind+1]], color='C3')
    axk.plot([-1, 1], [y, y], color='C3')
axk.plot([-1, 1], [kys[-1], kys[-1]], color='C3')
axk.text(0.9, 0.05, '$k_x$')
axk.text(0.05, 0.9, '$k_y$')
axk.set_xlim([-1.05, 1.05])
axk.set_ylim([-1.05, 1.05])
axk.set_xticklabels([])
axk.set_yticklabels([])

fig.savefig('epi.pdf', bbox_inches='tight', dpi=300)

