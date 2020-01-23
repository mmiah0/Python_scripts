## python script for plotting peak interstory drift (PID) vs.
## spectral amplitude at a building's first modal period

import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 25, 18
#style.use('ggplot')
from pylab import *
rc('axes', linewidth=5)

# read and manipulate spectra and drift files to map their pairs
# and write to a file
#f=open('driftvsjerk.txt','w')
with open('pulses.txt','r') as f1, open('40st_m7_fn_drift.txt', 'r') as f2:
 pulse=[]
 drift=[]
 for line1,line2 in zip(f1,f2):
   pulse.append(float(line1.split()[0]))
   drift.append(line2.split()[2])

plt.scatter(pulse, drift, s=175, color='blue', linewidth=1.5, label="0-10 km")
plt.title('Peak drift vs. number of pulses 3 story (M7.0-FN)',fontsize=50,fontname="Times New Roman Bold", y=1.05)
plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.xlabel('Number of pulses (PGA > 50 in/s2)', fontsize=50,fontname="Times New Roman Bold", labelpad=30)
plt.ylabel('Peak interstory drift (%)', fontsize=50,fontname="Times New Roman Bold", labelpad=30)
plt.xticks(fontsize=35)
plt.yticks(fontsize=35)
plt.grid(True)
#plt.legend(fontsize=35)
plt.show()
