# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 15:20:38 2021

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
t = np.arange(0, te * 2, t_step)

t2_envelope = nt.T2eq(t, t2, 1)
t2star_envelope_te_by_2 = nt.T2eq(t[t<te/2], t2star, 1)
t2star_envelope = np.concatenate((t2star_envelope_te_by_2, np.flip(t2star_envelope_te_by_2), nt.T2eq(t[t<te], t2star, 1)))
envelope = t2star_envelope * t2_envelope
sig = envelope * np.sin(f0 * t)

fig1, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex=True, figsize=(10, 7))

t_rf = np.arange(-50, te *2, t_step)
sinc = np.sin(t_rf[312:688]*0.5)/t_rf[312:688]
rf = np.zeros(len(t_rf))
rf[312:688] = sinc * 2
# rf[2312:2688] = sinc*2
ax1.plot(t_rf/10, rf, 'C1')
# ax1.text(10, 0.5, '$90^\circ$')
# ax1.text(210, 0.5, '$180 ^\circ$')
ax1.set_yticklabels([])
ax1.set_yticks([-10, 0, 10])
ax1.set_ylim([-0.3, 1.2])
ax1.set_ylabel('RF')
ax1.text(0.5, 0.5, 'Excitation')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>-25) & (t_grad<25)] = grad_amp
grad[(t_grad>25) & (t_grad<75)] = -grad_amp * 0.5
ax2.plot(t_grad/10, grad, 'C2')
ax2.set_yticklabels([])
ax2.set_yticks([-1, 0, 1])
ax2.set_ylim([-1.2, 1.2])
ax2.set_ylabel('$G_z$\nSlice')
ax2.text(-0, 0.2, 'Slice select', horizontalalignment='center')
ax2.text(5, -0.3, 'Rephase $z$', horizontalalignment='center')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
# grad[(t_grad>-25) & (t_grad<25)] = grad_amp
grad[(t_grad>25) & (t_grad<75)] = grad_amp
ax3.plot(t_grad/10, grad, 'C2')
ax3.plot(t_grad/10, grad*0.75, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, grad*0.50, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, grad*0.25, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, grad*0.00, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, grad*-0.25, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, grad*-0.50, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, grad*-0.75, 'C2', linestyle=(0, (1, 0.5)))
ax3.plot(t_grad/10, -grad, 'C2')
ax3.set_yticklabels([])
ax3.set_yticks([-1, 0, 1])
ax3.set_ylim([-1.2, 1.2])
ax3.set_ylabel('$G_y$\nPhase')
ax3.text(8, 0.2, 'Phase encode along $y$')

t_grad = np.arange(-50, te *2, t_step)
grad_amp = 1
grad = np.zeros(len(t_grad))
grad[(t_grad>75) & (t_grad<175)] = grad_amp
grad[(t_grad>25) & (t_grad<75)] = -grad_amp
ax4.plot(t_grad/10, grad, 'C2')
ax4.set_yticklabels([])
ax4.set_xticklabels([])
ax4.set_yticks([-1, 0, 1])
ax4.set_ylim([-1.2, 1.2])
ax4.set_ylabel('$G_x$\nFreq')
ax4.set_xlabel('Time')
ax4.text(5, -0.6, 'De-phase $x$', horizontalalignment='center')
ax4.text(12.5, 0.3, 'Frequency encode along $x$', horizontalalignment='center')
ax4.set_xlim([-5, 20])

fig1.savefig('signal_localisation_psd.eps', bbox_inches='tight', dpi=300)