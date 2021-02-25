# -*- coding: utf-8 -*-
"""
Created on Fri Feb  25 18:41:06 2021

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
t2 = 5000 # ms
t2star = 70 # ms
te = 450 # ms
f0 = 1#2.528
t_step = 0.1 # ms
t = np.around(np.arange(-5, te * 2, t_step), 1)
t_readout = 35
t_blip = 5

t_sig = t[t>=-0.05]
t2_envelope = nt.T2eq(t_sig, t2, 1)
t2star_envelope_te_by_2 = nt.T2eq(t_sig[t_sig<te], t2star, 1)
t2star_envelope = np.concatenate((np.flip(t2star_envelope_te_by_2), t2star_envelope_te_by_2))
envelope = t2star_envelope * t2_envelope
epi_echo = nt.T2eq(np.arange(0, t_readout/2, t_step), 7, 1) * np.sin(f0 * np.arange(0, t_readout/2, t_step))
epi_echo = np.concatenate((np.flip(-epi_echo), epi_echo))
sig = np.zeros(len(t_sig))
t0 = int(((te-4*t_readout)-t_readout/2)/t_step)
sig[t0:t0+len(epi_echo)*9] = np.tile(epi_echo, 9)
sig *= envelope

fig, axs = plt.subplots(ncols=1, nrows=5, sharex=True, figsize=(10, 7))
axrf = axs[0]
axgx = axs[3]
axgy = axs[2]
axgz = axs[1]
axsig= axs[4]

t_rf = np.arange(-50, te *4, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
rf = np.zeros(len(t_rf))
rf[312:688] = sinc * 1
rf[2812:3188] = sinc * 2
axrf.text(10, 0.5, '$90^\circ$')
axrf.text(130, 0.5, '$180 ^\circ$')
axrf.plot(t_rf/2, rf, 'C1')
axrf.plot([-100, -25], [0, 0], 'C1')
# axrf.axvspan(45, 205, color='C4', alpha=0.2)
axrf.set_yticklabels([])
axrf.set_yticks([-10, 0, 10])
axrf.set_ylim([-0.3, 1.2])
axrf.set_ylabel('RF')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>-13) & (t_grad<13)] = grad_amp
grad[(t_grad>13) & (t_grad<39)] = -grad_amp * 0.5
grad[(t_grad>115) & (t_grad<135)] = grad_amp
axgz.plot(t_grad, grad, 'C2')
# axgz.axvspan(45, 205, color='C4', alpha=0.2)
axgz.set_yticklabels([])
axgz.set_yticks([-1, 0, 1])
axgz.set_ylim([-1.2, 1.2])
axgz.set_ylabel('$G_z$\nSlice')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = -0.5
blip_amp = 0.2
diff_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>50) & (t_grad<100)] = diff_amp
grad[(t_grad>150) & (t_grad<200)] = diff_amp
grad[(t_grad>257.5) & (t_grad<292.5)] = grad_amp
for n in np.arange(-4, 4, 1):
    grad[(t_grad>(te-n*t_readout - t_readout/2)-t_blip/2) & (t_grad<(te-n*t_readout - t_readout/2)+t_blip/2)] = blip_amp
gy_cm = matplotlib.cm.plasma
trads = np.linspace(0, 1, 9)
trad_col = [gy_cm(x) for x in trads]
axgy.text(125, -1.3, 'Diffusion\nGradients', horizontalalignment='center')
axgy.plot(t_grad, grad, color='C2')
# axgy.axvspan(45, 205, color='C4', alpha=0.2)
axgy.set_yticklabels([])
axgy.set_yticks([-1, 0, 1])
axgy.set_ylim([-1.2, 1.2])
axgy.set_ylabel('$G_y$\nPhase')

t_grad = np.arange(-50, te *2, t_step)

grad_amp = 1
grad = np.zeros(len(t_grad))
# grad[(t_grad>te-t_readout/2) & (t_grad<te+t_readout/2)] = grad_amp
pol = -1
for n in np.arange(-4, 5, 1):
    grad[(t_grad>(te-n*t_readout)-t_readout/2) & (t_grad<(te-n*t_readout)+t_readout/2)] = pol * grad_amp
    pol *= -1
n=5
grad[(t_grad>(te-n*t_readout)-t_readout/2) & (t_grad<(te-n*t_readout)+t_readout/2)] = pol * grad_amp * 0.5
# grad[(t_grad>75) & (t_grad<175)] = grad_amp
# grad[(t_grad>25) & (t_grad<75)] = -grad_amp
axgx.plot(t_grad, grad, 'C2')
# axgx.axvspan(45, 205, color='C4', alpha=0.2)
# axgx.plot([7.5, 17.5], [1, 1], 'C3') # Acquisition
axgx.set_yticklabels([])
axgx.set_yticks([-1, 0, 1])
axgx.set_ylim([-1.2, 1.2])
axgx.set_ylabel('$G_x$\nFreq')
axgx.text(te, 0, 'EPI\nReadout', horizontalalignment='center', verticalalignment='center')

axsig.plot(t_sig, sig)
axsig.plot([-50, 0], [0, 0], 'C0')
# axsig.axvspan(45, 205, color='C4', alpha=0.2)
# axsig.axvspan(t0*t_step, t0*t_step + t_readout*9, color='C3', alpha=0.2) #Acquisition
axsig.set_xlabel('Time ($ms$)')
axsig.set_xlim([-50, 650])
axsig.set_yticklabels([])
axsig.set_xticklabels([])
axsig.set_ylabel('Signal')

fig.savefig('diffusion_psd_epi.pdf', bbox_inches='tight', dpi=300)

