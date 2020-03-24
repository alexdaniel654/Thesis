# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 11:41:31 2018

@author: Alex Daniel
"""
import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import nephtools as nt
import glob

#%% Inversion Recovery

t = np.linspace(0, 3000, 100)
T1 = 800.0
M0 = 1.0
Mz = nt.T1eq(t, T1, M0)

TI = np.array([250,350,400,500,750,900,1100,1300,1500,2000,3000])
ind = [0, 3, 4, 5, 6, 7, 8, 9, 10]
TI = np.array([TI[i] for i in ind])
MzTI = nt.T1eq(TI, T1, M0)

plt.plot(t, Mz, label='True Signal')
plt.plot(t, np.abs(Mz), '--', label='Measured Signal')
plt.plot(TI, MzTI, 'C0x')
plt.plot(TI, np.abs(MzTI), 'C1x')
plt.xlabel('Time (ms)')
plt.ylabel('Mz (AU)')
plt.legend()
plt.grid()

plt.savefig('signal_correction.eps', bbox_inches='tight', transparent=True)
plt.savefig('signal_correction.png',dpi=500, bbox_inches='tight', transparent=True)

#%% Smodding
files = glob.glob('D:\\ppxad2\\OwnCloud\\University\\Renal Imaging\\Nephrectomy\\Data\\20171221\\7T\\PARREC\\Neph_2week_7T_WIP_T1_TI*.PAR')
TI = np.array([250,350,400,500,750,900,1100,1300,1500,2000,3000])
data = nt.importscaled(files)
data_smod = nt.smod(data)
#%%
x = 150
y = 125
plt.plot(np.pi*(data[x,y,20,:,0]/np.max(data[x,y,20,:,0])),'x', label = 'Modulus')
plt.plot(data[x,y,20,:,3],'x', label = 'Phase')
plt.legend()
plt.grid()

#%%

T1_0 = 1000
dT1 = 20/60.0 #in ms/sec
scan_time = 270.0 #sec
M0 = 1.0
TI_1 = np.array([400, 500, 750, 900, 1100, 2600])
TI_2 = np.array([2600, 400, 500, 1100, 750, 900])
t = np.linspace(0, TI_1.max(), 100)

Mz_1 = np.zeros(6)
Mz_2 = np.zeros(6)
T1_arr = np.zeros(6)
T1_arr[0] = T1_0
for n in np.arange(1, len(T1_arr)):
    T1_arr[n] = T1_arr[n-1] - (dT1 * scan_time)

T1_mean = T1_arr.mean()

for n in np.arange(len(T1_arr)):
    Mz_1[n] = nt.T1eq(TI_1[n], T1_arr[n], M0)
    Mz_2[n] = nt.T1eq(TI_2[n], T1_arr[n], M0)
    
T1_1 = nt.T1fit(Mz_1, TI_1)
T1_2 = nt.T1fit(Mz_2, TI_2)

T1_err = (T1_1[0]-T1_0, T1_2[0]-T1_0)

Mz_fit_1 = nt.T1eq(t, T1_1[0], T1_1[1])
Mz_fit_2 = nt.T1eq(t, T1_2[0], T1_2[1])
Mz_fit_mean = nt.T1eq(t, T1_0, M0)
plt.close()
plt.plot(TI_1, Mz_1, 'xC0', label = 'Assending TI')
plt.plot(TI_2, Mz_2, 'xC1', label = 'Randomised TI')
plt.plot(t, Mz_fit_1, '--C0')
plt.plot(t, Mz_fit_2, '--C1')
plt.plot(t, Mz_fit_mean, '--C2')
plt.xlabel('Time (ms)')
plt.ylabel('Mz (AU)')
plt.legend()
plt.grid()
