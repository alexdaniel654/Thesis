# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 15:09:40 2021
@author: Alex Daniel
"""

import nephtools as nt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from scipy.signal import resample
import seaborn as sns
sns.set()
sns.set_context('talk')
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
t2 = 1000 # ms
t2star = 70 # ms
te = 500 # ms
f0 = 6.2
t_step = 0.1 # ms
t = np.around(np.arange(-5, te * 4, t_step), 1)
t_readout = 50
t_pe = 5
t_blip = 5
t_r0 = 50
t_es = 100
etl = 19

t_sig = t[t>=-0.05]
t2_envelope = nt.T2eq(t_sig, t2, 1)
echo = nt.T2eq(np.arange(0, t_readout/2, t_step), 5, 1) * np.cos(f0 * np.arange(0, t_readout/2, t_step))
echo = np.concatenate((np.flip(echo), echo))[:-1]
sig = np.zeros(len(t_sig))
for ind in np.arange(etl):
    sig[(t_sig>(t_r0 + (t_es * ind) + t_es/2 - t_readout/2)) & (t_sig<(t_r0 + (t_es * ind) + t_es/2 + t_readout/2))] = echo

sig *= t2_envelope

cm = matplotlib.cm.plasma
echo_col = [cm(x) for x in np.linspace(0, 1, etl)]

fig, axs = plt.subplots(ncols=2, nrows=4, sharex=True, figsize=(14, 7))
gs = axs[0, 1].get_gridspec()
for ax in axs[:, 1]:
    ax.remove()
axk = fig.add_subplot(gs[:, 1])
axrf = axs[0, 0]
axgx = axs[3, 0]
axgy = axs[2, 0]
axgz = axs[1, 0]
# axsig= axs[4, 0]

t_rf = np.arange(-50, te * 4, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
sinc = resample(sinc, int(20/t_step))
rf = np.zeros(len(t_rf))
rf[(t_rf>-10) & (t_rf<10)] = sinc
for ind in np.arange(etl):
    rf[(t_rf>(t_r0 + t_es * ind)) & (t_rf<(t_r0 + t_es * ind + 20))] = sinc * 2
    axrf.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axrf.plot(t_rf, rf, 'C1')
axrf.set_yticklabels([])
axrf.set_yticks([-10, 0, 10])
axrf.set_ylim([-0.3, 1.2])
axrf.set_ylabel('RF')

t_grad = np.arange(-50, te * 4, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>-13) & (t_grad<13)] = grad_amp
grad[(t_grad>13) & (t_grad<39)] = -grad_amp * 0.5
for ind in np.arange(etl):
    grad[(t_grad>(t_r0 + t_es * ind)) & (t_grad<(t_r0 + t_es * ind + 20))] = grad_amp
    axgz.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axgz.plot(t_grad, grad, 'C2')
axgz.set_yticklabels([])
axgz.set_yticks([-1, 0, 1])
axgz.set_ylim([-1.2, 1.2])
axgz.set_ylabel('$G_z$\nSlice')

t_grad = np.arange(-50, te * 4, t_step)
grad_amp = 1
pe_amp = np.linspace(-1, 0.5, etl)
grad = np.zeros(len(t_grad))
for ind, amp in enumerate(pe_amp):
    grad[(t_grad>(t_r0 + (t_es * ind) + t_es/2 - t_readout/2 - t_pe)) & (t_grad<(t_r0 + (t_es * ind) + t_es/2 - t_readout/2))] = grad_amp * amp
    grad[(t_grad>(t_r0 + (t_es * ind) + t_es/2 + t_readout/2)) & (t_grad<(t_r0 + (t_es * ind) + t_es/2 + t_readout/2 + t_pe))] = grad_amp * -amp
    axgy.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axgy.plot(t_grad, grad, color='C2')
axgy.set_yticklabels([])
axgy.set_yticks([-1, 0, 1])
axgy.set_ylim([-1.2, 1.2])
axgy.set_ylabel('$G_y$\nPhase')

t_grad = np.arange(-50, te * 4, t_step)

grad_amp = 1
grad = np.zeros(len(t_grad))
# grad[(t_grad>te-t_readout/2) & (t_grad<te+t_readout/2)] = grad_amp
# grad[(t_grad>75) & (t_grad<175)] = grad_amp
# grad[(t_grad>25) & (t_grad<75)] = -grad_amp
for ind in np.arange(etl):
    grad[(t_grad>(t_r0 + (t_es * ind) + t_es/2 - t_readout/2)) & (t_grad<(t_r0 + (t_es * ind) + t_es/2 + t_readout/2))] = grad_amp
    axgx.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axgx.plot(t_grad, grad, 'C2')
axgx.set_xlim([-50, 2000])
axgx.set_xlabel('Time ($ms$)')
axgx.set_xticklabels([])
axgx.set_yticklabels([])
axgx.set_yticks([-1, 0, 1])
axgx.set_ylim([-1.2, 1.2])
axgx.set_ylabel('$G_x$\nFreq')

# axsig.plot(t_sig, sig)
# axsig.plot([-50, 0], [0, 0], 'C0')
# for ind in np.arange(etl):
#     axsig.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
# axsig.set_xlabel('Time ($ms$)')
# # axsig.set_xlim([-50, 650])
# axsig.set_yticklabels([])
# # axsig.set_xticklabels([])
# axsig.set_ylabel('Signal')

kx, ky = [[-1, 0], [0, -1]]
ku, kv = [[2, 0], [0, 2]]
axk.quiver(kx, ky, ku, kv, color="k", scale_units='xy', angles='xy', scale=1)
kys = np.linspace(-1, 0.5, etl)
# axk.plot([0, -1], [0, -1], 'C3')
for ind, y in enumerate(kys[:-1]):
#     side = ((ind % 2) * -2) + 1
#     axk.plot([side, side], [y, kys[ind+1]], color='C3')
    axk.plot([-1, 1], [y, y], color=echo_col[ind])
axk.plot([-1, 1], [kys[-1], kys[-1]], color=echo_col[-1])
axk.text(0.9, 0.05, '$k_x$')
axk.text(0.05, 0.9, '$k_y$')
axk.set_xlim([-1.05, 1.05])
axk.set_ylim([-1.05, 1.05])
axk.set_xticklabels([])
axk.set_yticklabels([])

fig.savefig('haste.pdf', bbox_inches='tight', dpi=300)

