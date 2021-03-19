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

fig, axs = plt.subplots(ncols=1, nrows=3, sharex=True, figsize=(10, 4.8*(3/2)))
axrf = axs[0]
axg = axs[1]
axp = axs[2]


t_rf = np.arange(-50, te *4, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
rf = np.zeros(len(t_rf))
rf[312:688] = sinc * 1
rf[2812:3188] = sinc * 2
axrf.text(10, 0.5, '$90^\circ$')
axrf.text(130, 0.5, '$180 ^\circ$')
axrf.plot([-100, -25], [0, 0], 'C1')
axrf.plot(t_rf/2, rf, 'C1')
# axrf.axvspan(45, 205, color='C4', alpha=0.2)
axrf.set_yticklabels([])
axrf.set_yticks([-10, 0, 10])
axrf.set_ylim([-0.3, 1.2])
axrf.set_ylabel('RF')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = -0.5
blip_amp = 0.2
diff_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>50) & (t_grad<112)] = diff_amp
grad[(t_grad>138) & (t_grad<200)] = diff_amp
grad[(t_grad>257.5) & (t_grad<292.5)] = grad_amp
for n in np.arange(-4, 4, 1):
    grad[(t_grad>(te-n*t_readout - t_readout/2)-t_blip/2) & (t_grad<(te-n*t_readout - t_readout/2)+t_blip/2)] = blip_amp
# axg.text(125, -1.3, 'Diffusion\nGradients', horizontalalignment='center')
axg.plot(t_grad, grad, color='C2')
# axg.axvspan(45, 205, color='C4', alpha=0.2)
axg.set_yticklabels([])
axg.set_yticks([-1, 0, 1])
axg.set_ylim([-1.2, 1.2])
axg.set_ylabel('$G_{diff}$')
axg.annotate('G', (45, diff_amp), (45, diff_amp/2), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))
axg.annotate('G', (45, 0), (45, diff_amp/2), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))

axg.annotate('$\delta$', (50, 0.7), (81, 0.7), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))
axg.annotate('$\delta$', (112, 0.7), (81, 0.7), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))

axg.annotate('$\Delta$', (50, -0.3), (94, -0.3), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))
axg.annotate('$\Delta$', (138, -0.3), (94, -0.3), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))

t_phase = np.arange(-50, te *2, t_step)
stationary = np.zeros(len(t_phase))
diffusing = np.zeros(len(t_phase))
mask = np.zeros(len(t_phase))
for n, t in enumerate(t_phase):
    if t<50:
        mask[n] = 1
        # diffusing[n] = 0.0001
    if (t>50) & (t<112):
        stationary[n] = stationary[n-1] + grad[n]*0.001
        diffusing[n] = diffusing[n-1] + grad[n]*1E-6*t**1.5
        mask[n] = 1
    if np.abs(t-138)<0.05:
        stationary[n] = -stationary[mask==1][-1]
        diffusing[n] = -diffusing[mask==1][-1]
        mask[n] = 1
    if (t>138.05) & (t<200):
        stationary[n] = stationary[n-1] + grad[n]*0.001
        diffusing[n] = diffusing[n-1] + grad[n]*1E-6*t**1.5
        # diffusing[n] = diffusing[n-1] + grad[n]*0.0001 + grad[n]*t
        mask[n] = 1
    if t>200:
        stationary[n] = stationary[n-1]
        diffusing[n] = diffusing[n-1]
        mask[n] = 1
# stationary[(t_phase>50) & (t_phase<100)] = t_phase[(t_phase>50) & (t_phase<100)]
axp.plot(t_phase[mask==1], stationary[mask==1], 'C0', label='Stationary')
axp.plot(t_phase[mask==1], diffusing[mask==1], 'C3', label='Diffusing')
# axgz.axvspan(45, 205, color='C4', alpha=0.2)
axp.legend(loc='upper left')
axp.set_yticklabels([])
axp.set_yticks([-1, 0, 1])
axp.set_ylim([-1.2, 1.2])
axp.set_ylabel('Phase')
axp.set_xlabel('Time ($ms$)')
axp.set_xlim([-50, 250])
axp.set_xticklabels([])



fig.savefig('diffusion_psd.pdf', bbox_inches='tight', dpi=300)

