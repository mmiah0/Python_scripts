#!/bin/bash
f=open('fppgd.txt','r')
x=[]
y=[]
d=[]
for line in f:
  x.append(line.split()[0][3:5])
  y.append(line.split()[0][0:2])
  d.append(line.split()[1])

f=open('fpd.txt','w')
for item in zip(x, y, d):
  val=' '.join(map(str,item))
  f.write(str(val).strip("()")+'\n')
f.close()

import pylab
import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate
from scipy import ndimage
from pylab import rcParams
rcParams['figure.figsize'] = 20, 7

N = 1000 #number of points for plotting/interpolation

x, y, z = np.genfromtxt(r'fpd.txt', unpack=True)

xi = np.linspace(x.min(), x.max(), N)
yi = np.linspace(y.min(), y.max(), N)
zi = scipy.interpolate.griddata((x, y), z, (xi[None,:], yi[:,None]), method='cubic')

import matplotlib.colors as colors
minvalue=min(z)
maxvalue=max(z)
print maxvalue
smooth=np.linspace(0,3.5,4, endpoint=True)
smooth=[0.0,0.1,0.2,0.3,0.4,0.5,0.6]
cmap = colors.ListedColormap(['green','yellow','gold','orange','r','darkred'])
bounds=[0.0,0.1,0.2,0.3,0.4,0.5,0.6]
norm = colors.BoundaryNorm(bounds, cmap.N)
#plt.figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
#fig = plt.figure()
im=plt.contourf(xi, yi, abs(zi), smooth, cmap=cmap, norm=norm, extend='max', rotation=90)

# uncomment the following to add space between tick labels and the axes
#plt.tick_params(axis='both', which='major', pad=15)
plt.xlabel("Parallel to the fault, Y (Km)", fontsize=50, labelpad=45)
plt.ylabel("Normal to the fault, X (Km)", fontsize=50, labelpad=45)
plt.title('Peak ground displacement for M6.5 (5Hz) FP motions ', y=1.1, fontsize=50)
plt.xticks(fontsize=40)
plt.yticks(fontsize=40)
plt.axis('scaled')
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=18)
#plt.colorbar()

## Use this block to translate the origin to the upper left corner
#ax=plt.gca()                            # get the axis
#ax.set_ylim(ax.get_ylim()[::-1])        # invert the axis
#ax.set_xlim(ax.get_xlim()[::1])        # invert the axis
#ax.xaxis.tick_top() 
#ax.xaxis.set_tick_params(labelsize=20)
                   # and move the X-Axis      
#ax.yaxis.set_ticks(np.arange(0, 16, 1)) # set y-ticks
#ax.yaxis.tick_left()                    # remove right y-Ticks

from matplotlib import ticker
import matplotlib.colors as colors

#cmap = colors.ListedColormap(['g','y','r'])
bounds=[0.0,0.1,0.2,0.3,0.4,0.5,0.6]
norm = colors.BoundaryNorm(bounds, cmap.N)
cb = plt.colorbar(im,norm=norm, boundaries=bounds, ticks=[0.0,0.1,0.2,0.3,0.4,0.5,0.6],)
#tick_locator = ticker.MaxNLocator(nbins=4)
#cb.locator = tick_locator
#cb.update_ticks()
cb.set_label('Displacement (m)', size=40, labelpad=40)
cb.ax.tick_params(size=30,labelsize=40, pad = 15)
#plt.savefig('13st_fnormal.pdf')
plt.show()

## see the list of colors in this link:
## http://stackoverflow.com/questions/22408237/named-colors-in-matplotlib
