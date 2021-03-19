# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:14:19 2020

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
t2 = 500 # ms
t2star = 20 # ms
te = 200 # ms
f0 = 2
t_step = 0.1 # ms
t = np.arange(0, te * 1.5, t_step)

t2_envelope = nt.T2eq(t, t2, 1)
t2star_envelope_te_by_2 = nt.T2eq(t[t<te/2], t2star, 1)
t2star_envelope = np.concatenate((t2star_envelope_te_by_2, np.flip(t2star_envelope_te_by_2), t2star_envelope_te_by_2))
envelope = t2star_envelope * t2_envelope
sig = envelope * np.sin(f0 * t)

fig1, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(10, 4.8))
ax1.plot(t, sig, label='Signal', lw=1.5)
ax1.plot([-50, 0], [0, 0], color='C0', lw=1.5)
ax1.plot(t, t2_envelope, 'k:', label='$T_2$ Envelope')
ax1.plot(t[t<te/2], t2star_envelope[t<te/2], 'k-.', label='$T_2*$ Envelope')

ax1.set_ylabel('Signal')
ax1.set_yticklabels([])
ax1.set_ylim([-1.1, 1.1])
# ax1.legend()
ax1.text(15, 0.5, '$T_2^*$ Envelope')
ax1.text(240, 0.70, '$T_2$ Envelope')
ax1.set_xlim([-50, 300])

t_rf = np.arange(-50, te *1.5, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
rf = np.zeros(len(t_rf))
rf[312:688] = sinc
rf[1312:1688] = sinc*2
ax2.plot(t_rf, rf, 'C1')
ax2.text(10, 0.5, '$90^\circ$')
ax2.text(110, 0.5, '$180 ^\circ$')
ax2.set_yticklabels([])
ax2.set_yticks([-10, 0, 10])
ax2.set_ylim([-0.3, 1.2])
ax2.set_ylabel('RF')
ax2.set_xlabel('Time ($ms$)')

# ax2.arrow(0, 1, 200, 0, color='k', width=0.01, length_includes_head=True, head_width=0.2, head_length=0.2)
te_label_height = 1.2
ax2.annotate('TE', (200, te_label_height), (100, te_label_height), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))
ax2.annotate('TE', (0, te_label_height), (100, te_label_height), 
             horizontalalignment='center', verticalalignment='center', 
             arrowprops=dict(arrowstyle='-|>', color='k'))

fig1.savefig('se_signal.eps', bbox_inches='tight', dpi=300)