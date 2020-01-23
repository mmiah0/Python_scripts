# building_regression.py

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

accfile = 'parallelpgv.txt'
pidfile = '20st_parallel.txt'

name, acc = np.loadtxt(accfile, dtype=[ ('name', 'S'), ('acc', 'f8')], unpack=True)
i,j,pid = np.loadtxt(pidfile, dtype=[ ('i', 'S'), ('j', 'S'), ('pid', 'f8')], unpack=True)

x = np.array(acc)
y = np.array(pid)

r = scipy.stats.stats.pearsonr(x,y)
print ('linear correlation: ', r)

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(x,y)
print('scipy output:')
print('intercept: ', intercept)
print('slope: ', slope)
print('std_err: ', std_err)
print ('r :', r_value)

# Make figure
fig = plt.figure(figsize=(10,8), dpi=800)
# First panel
ax1 = fig.add_subplot(211)
ax1.set_xlim(0, x.max())
ax1.set_ylim(0,y.max())
ax1.set_xlabel('PGA, in/s/s')
ax1.set_ylabel('PID, %')
ax1.scatter(x,y, marker='o', s=10, c='b')
xx = np.linspace(x.min(), x.max())
ax1.plot(xx, intercept + slope*xx, ls='-', c='b', lw=3)
ax1.set_title('Raw data and regression')

# Second panel
ax2 = fig.add_subplot(212)
ax2.set_xlim(0, x.max())
ax2.set_xlabel('PGA, in/s/s')
ax2.set_ylabel('PID residual, %')
dy = y - (intercept + slope*x)
ax2.scatter(x,dy, marker='o', s=10, c='b')
ax2.grid()
ax2.set_title('Residuals')

plt.savefig('PID_vs_PGA_regression.png')




