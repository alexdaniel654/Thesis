# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 17:48:12 2020

@author: Alex Daniel
"""
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})
 
#%% Lab Frame   
fig1 = plt.figure(figsize=plt.figaspect(0.5))
ax1 = fig1.add_subplot(1, 1, 1, projection='3d')
ax1.view_init(30, 45)
ax1.grid(False)
ax1.axis(False)

# Axis
x, y, z = np.array([[-1.5,0,0],[0,-1.5,0],[0,0,-1.5]])
u, v, w = np.array([[3,0,0],[0,3,0],[0,0,3]])
ax1.quiver(x,y,z,u,v,w,arrow_length_ratio=0.05, color="k", zorder=1)
ax1.text(0.1, 1.6, 0, '$y$')
ax1.text(1.7, 0, 0, '$x$')
ax1.text(0, -0.05, 1.55, '$z$')

# Vector Path
points = 500
theta = np.linspace(0, -12 * np.pi, points)
z = np.cos(np.linspace(0, np.pi/2, points))
r = np.sin(np.linspace(0, np.pi/2, points))
x = r * np.sin(theta)
y = r * np.cos(theta)
ax1.plot(x, y, z, color='C0', zorder=3)

# Vector
x, y, z = np.array([0,0,0])
vector = np.array([-0.5,1,0.3])
u, v, w = vector/np.sqrt(np.sum(vector ** 2))
ax1.quiver(x,y,z,u,v,w,arrow_length_ratio=0.3, color="C1")
ax1.text(u-0.05, v+0.05, w-0.1, '$\mu$', zorder=2)

# B0
x, y, z = np.array([0.7,-0.7,1])
u, v, w = np.array([0,0,1])
# u, v, w = vector/np.sqrt(np.sum(vector ** 2))
ax1.quiver(x,y,z,u,v,w,arrow_length_ratio=0.2, color="C2")
ax1.text(x + u -0.05, y + v+0.05, z + w-0.2, '$B_0$', zorder=3)

# B1
x, y, z = np.array([0,0,0])
u, v, w = np.array([1.2,0,0])
# u, v, w = vector/np.sqrt(np.sum(vector ** 2))
ax1.quiver(x,y,z,u,v,w,arrow_length_ratio=0.2, color="C2", zorder=3)
ax1.text(u-0.05, v+0.05, w-0.2, '$B_1$')

fig1.savefig('lab_frame.eps', bbox_inches='tight', pad_inches=-0.3,
             dpi=300, transparent=True)
plt.show()

#%% Rotating Frame
fig2 = plt.figure(figsize=plt.figaspect(0.5))
ax2 = fig2.add_subplot(1, 1, 1, projection='3d')
ax2.view_init(30, 45)
ax2.grid(False)
ax2.axis(False)

# Axis
x, y, z = np.array([[-1.5,0,0],[0,-1.5,0],[0,0,-1.5]])
u, v, w = np.array([[3,0,0],[0,3,0],[0,0,3]])
ax2.quiver(x,y,z,u,v,w,arrow_length_ratio=0.05, color="black", zorder=1)
ax2.text(0.1, 1.6, 0, '$y\'$')
ax2.text(1.7, 0, 0, '$x\'$')
ax2.text(0, -0.05, 1.55, '$z\'$')

# Vector Path
points = 500
theta = np.linspace(0, np.pi/2, points)
z = np.cos(theta)
x = np.zeros(points)
y = np.sin(theta)
ax2.plot(x, y, z, color='C0', zorder=3)

# Vector
x, y, z = np.array([0,0,0])
vector = np.array([-0,1,0.3])
u, v, w = vector/np.sqrt(np.sum(vector ** 2))
ax2.quiver(x,y,z,u,v,w,arrow_length_ratio=0.3, color="C1")
ax2.text(u-0.05, v+0.05, w-0.1, '$\mu$')

# B0
x, y, z = np.array([0.7,-0.7,1])
u, v, w = np.array([0,0,1])
# u, v, w = vector/np.sqrt(np.sum(vector ** 2))
ax2.quiver(x,y,z,u,v,w,arrow_length_ratio=0.2, color="C2", zorder=3)
ax2.text(x + u -0.05, y + v+0.05, z + w-0.2, '$B_0$')

# B1
x, y, z = np.array([0,0,0])
u, v, w = np.array([1.2,0,0])
# u, v, w = vector/np.sqrt(np.sum(vector ** 2))
ax2.quiver(x,y,z,u,v,w,arrow_length_ratio=0.2, color="C2", zorder=3)
ax2.text(u-0.05, v+0.05, w-0.2, '$B_1$')



fig2.savefig('rotating_frame.eps', bbox_inches='tight', pad_inches=-0.3,
             dpi=300, transparent=True)
