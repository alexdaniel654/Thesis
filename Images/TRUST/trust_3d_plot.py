# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:22:10 2020

@author: Alex Daniel
"""

import nephtools as nt
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import progressbar
import seaborn as sns
sns.set()

#%% 3D Plot
res = 100
t2 = np.linspace(50, 180, res)
hct = np.linspace(0.3, 0.9, res)

t2mesh, hctmesh = np.meshgrid(t2, hct)
yvmesh = np.zeros(np.shape(t2mesh))
bar = progressbar.ProgressBar(maxval=len(t2) * len(hct),
                                  widgets=['Calculating Oxygenation ',
                                            progressbar.Bar('=', '[', ']'), ' ',
                                            progressbar.Percentage(), ' ', progressbar.AdaptiveETA()])
n=0
for x in range(len(t2)):
    for y in range(len(hct)):
        yvmesh[y,x] = nt.T2_to_Yv(t2[x], hct[y])
        bar.update(n)
        n += 1

yvmesh *= 100
bar.finish()
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.style.use(['seaborn-dark', 'default'])
surf = ax.plot_surface(hctmesh, t2mesh, yvmesh, cmap=cm.inferno, linewidth=0, antialiased=True)
ax.set_xlabel('Hct')
ax.set_ylabel('$T_2$ (ms)')
ax.set_zlabel('Blood Oxygenation (%)')
plt.tight_layout()
plt.savefig('Empirical_surf.eps', dpi=300, transparent=True)
plt.savefig('Empirical_surf.png', dpi=300, transparent=True)

#%% 2D Plot
t2 = np.linspace(30, 180, 100)
hct = np.linspace(0.3, 1, 8)
t2mesh, hctmesh = np.meshgrid(t2, hct)
yvmesh = np.zeros(np.shape(t2mesh))
bar = progressbar.ProgressBar(maxval=len(t2) * len(hct),
                                  widgets=['Calculating Oxygenation ',
                                            progressbar.Bar('=', '[', ']'), ' ',
                                            progressbar.Percentage(), ' ', progressbar.AdaptiveETA()])
n=0
for x in range(len(t2)):
    for y in range(len(hct)):
        yvmesh[y,x] = nt.T2_to_Yv(t2[x], hct[y])
        bar.update(n)
        n += 1

yvmesh *= 100
bar.finish()
#%%
def multiline(xs, ys, c, ax=None, **kwargs):
    from matplotlib.collections import LineCollection
    """Plot lines with different colorings

    Parameters
    ----------
    xs : iterable container of x coordinates
    ys : iterable container of y coordinates
    c : iterable container of numbers mapped to colormap
    ax (optional): Axes to plot on.
    kwargs (optional): passed to LineCollection

    Notes:
        len(xs) == len(ys) == len(c) is the number of line segments
        len(xs[i]) == len(ys[i]) is the number of points for each line (indexed by i)

    Returns
    -------
    lc : LineCollection instance.
    """

    # find axes
    ax = plt.gca() if ax is None else ax

    # create LineCollection
    segments = [np.column_stack([x, y]) for x, y in zip(xs, ys)]
    lc = LineCollection(segments, **kwargs)

    # set coloring of line segments
    #    Note: I get an error if I pass c as a list here... not sure why.
    lc.set_array(np.asarray(c))

    # add lines to axes and rescale 
    #    Note: adding a collection doesn't autoscalee xlim/ylim
    ax.add_collection(lc)
    ax.autoscale()
    return lc
fig, ax = plt.subplots()
lc = multiline(np.tile(t2, (8,1)), yvmesh, c=hct, cmap='Blues')
axcb = fig.colorbar(lc)
axcb.set_label('Haematocrit')
ax.set_xlabel('$T_2$ (ms)')
ax.set_ylabel('Oxygen Saturation (%)')
#%%
colors=cm.inferno(np.linspace(0, 1, yvmesh.shape[0]))
for x in range(yvmesh.shape[0]):
    plt.plot(t2, yvmesh[x,:], color=colors[x])