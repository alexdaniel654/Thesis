# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 17:39:13 2021
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
te = 1000 # ms
f0 = 6.2
t_step = 0.1 # ms
t = np.around(np.arange(-5, te * 4, t_step), 1)
t_readout = 50
t_pe = 20
t_blip = 5
t_r0 = 250
t_es = 150
etl = 16
n_startup = 3

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

fig, axs = plt.subplots(ncols=1, nrows=4, sharex=True, figsize=(14, 7))
# gs = axs[0, 1].get_gridspec()
# for ax in axs[:, 1]:
#     ax.remove()
# axk = fig.add_subplot(gs[:, 1])
axrf = axs[0]
axgx = axs[3]
axgy = axs[2]
axgz = axs[1]
# axsig= axs[4, 0]

t_rf = np.arange(-50, te * 4, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
sinc = resample(sinc, int(30/t_step))
rf = np.zeros(len(t_rf))
rf[(t_rf>-15) & (t_rf<15)] = sinc * 2
axrf.text(15, 0.7, '$180 ^\circ$', horizontalalignment='left')
for ind in np.arange(etl + n_startup):
    rf[(t_rf>(t_r0 + t_es * ind)) & (t_rf<(t_r0 + t_es * ind + 30))] = sinc * 0.25
    axrf.text(t_r0 + t_es * ind + 15, 0.25, r'$\alpha$', horizontalalignment='center')
    # axrf.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axrf.plot(t_rf, rf, 'C1')
axrf.axvspan(t_r0, t_r0 + t_es * n_startup, color='C0', alpha=0.2)
axrf.axvspan(t_r0 + t_es * n_startup, t_r0 + t_es * n_startup + t_es * etl, color='C3', alpha=0.2)
axrf.set_yticklabels([])
axrf.set_yticks([-10, 0, 10])
axrf.set_ylim([-0.3, 1.2])
axrf.set_ylabel('RF')

t_grad = np.arange(-50, te * 4, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>-13) & (t_grad<13)] = grad_amp
grad[(t_grad>13) & (t_grad<39)] = -grad_amp * 0.5
for ind in np.arange(etl + n_startup):
    grad[(t_grad>(t_r0 + t_es * ind)) & (t_grad<(t_r0 + t_es * ind + 30))] = grad_amp
    grad[(t_grad>(t_r0 + t_es * ind+40)) & (t_grad<(t_r0 + t_es * ind + 60))] = - 0.5 * grad_amp
    # axgz.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axgz.plot(t_grad, grad, 'C2')
axgz.axvspan(t_r0, t_r0 + t_es * n_startup, color='C0', alpha=0.2)
axgz.axvspan(t_r0 + t_es * n_startup, t_r0 + t_es * n_startup + t_es * etl, color='C3', alpha=0.2)
axgz.set_yticklabels([])
axgz.set_yticks([-1, 0, 1])
axgz.set_ylim([-1.2, 1.2])
axgz.set_ylabel('$G_z$\nSlice')

t_grad = np.arange(-50, te * 4, t_step)
grad_amp = 1
pe_startup_amp = np.ones(n_startup) * -1
pe_ro_amp = np.linspace(-1, 1, etl)
pe_amp = np.concatenate((pe_startup_amp, pe_ro_amp))
grad = np.zeros(len(t_grad))
for ind, amp in enumerate(pe_amp):
    grad[(t_grad>(t_r0 + t_es * ind+40)) & (t_grad<(t_r0 + t_es * ind + 60))] = grad_amp * amp
    # grad[(t_grad>(t_r0 + (t_es * ind) + t_es/2 + t_readout/2)) & (t_grad<(t_r0 + (t_es * ind) + t_es/2 + t_readout/2 + t_pe))] = grad_amp * -amp
    # axgy.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axgy.plot(t_grad, grad, color='C2')
axgy.axvspan(t_r0, t_r0 + t_es * n_startup, color='C0', alpha=0.2)
axgy.axvspan(t_r0 + t_es * n_startup, t_r0 + t_es * n_startup + t_es * etl, color='C3', alpha=0.2)
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
for ind in np.arange(etl + n_startup):
    grad[(t_grad>(t_r0 + t_es * ind+40)) & (t_grad<(t_r0 + t_es * ind + 60))] = - 0.5 * grad_amp
    grad[(t_grad>(t_r0 + t_es * ind+100)) & (t_grad<(t_r0 + t_es * ind + 125))] = grad_amp
    # axgx.axvspan(t_r0 + (t_es * ind) + t_es/2 - t_readout/2, t_r0 + (t_es * ind) + t_es/2 + t_readout/2, color=echo_col[ind], alpha=0.2) #Acquisition
axgx.plot(t_grad, grad, 'C2')
axgx.axvspan(t_r0, t_r0 + t_es * n_startup, color='C0', alpha=0.2)
axgx.axvspan(t_r0 + t_es * n_startup, t_r0 + t_es * n_startup + t_es * etl, color='C3', alpha=0.2)
axgx.set_xlim([-50, t_r0 + ((etl + n_startup) * t_es)])
axgx.set_xlabel('Time ($ms$)')
axgx.set_xticklabels([])
axgx.set_yticklabels([])
axgx.set_yticks([-1, 0, 1])
axgx.set_ylim([-1.2, 1.2])
axgx.set_ylabel('$G_x$\nFreq')



fig.savefig('tfe.pdf', bbox_inches='tight', dpi=300)

