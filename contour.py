#!/bin/bash
import pylab

import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate

N = 1000 #number of points for plotting/interpolation

x, y, z = np.genfromtxt(r'com.txt', unpack=True)

xi = np.linspace(x.min(), x.max(), N)
yi = np.linspace(y.min(), y.max(), N)
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

import matplotlib.colors as colors
minvalue=min(z)
maxvalue=max(z)
print maxvalue
smooth=np.linspace(0,2.5,25, endpoint=True)
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
#fig = plt.figure()
plt.contourf(xi, yi, zi, smooth, extend='max')

# uncomment the following to add space between tick labels and the axes
#plt.tick_params(axis='both', which='major', pad=15)
plt.xlabel("Parallel to the fault, Y (Km)", fontsize=30, labelpad=25)
plt.ylabel("Normal to the fault, X (Km)", fontsize=30, labelpad=25)
plt.title('Peak interstory drift of a 40 story building for fault-parallel component of ground motion', y=1.05, fontsize=30)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.axis('scaled')
#plt.colorbar()

from matplotlib import ticker

# (generate plot here)

cb = plt.colorbar()
tick_locator = ticker.MaxNLocator(nbins=4)
cb.locator = tick_locator
cb.update_ticks()
cb.set_label('Drift raito (%)', size=30, labelpad=20)
cb.ax.tick_params(size=30,labelsize=25)
#plt.savefig('13st_fnormal.pdf')
plt.show()
