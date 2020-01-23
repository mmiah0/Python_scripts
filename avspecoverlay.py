## python script for plotting ground acceleration, velocity, and displacement

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 35, 15
from pylab import *
rc('axes', linewidth=5)
#style.use('ggplot')

# Read first acc. file in pandas and set column names
f1=open('/home/mmiah/Documents/investigate/new_plots/m7/S_07_17/accspec','r')
df1 = pd.read_csv(f1, sep="\s+", header=3, names=['time1','acc1'])
#print df
# slice time and acceleration columns for plotting ground motion time history
#time=df.loc[:,"time"]
acc1=df1.loc[:,"acc1"] 

# Read second acc. file in pandas and set column names
f2=open('/home/mmiah/Documents/investigate/new_plots/m65/S_07_22/accspec','r')
df2 = pd.read_csv(f2, sep="\s+", header=3, names=['time','acc2'])
#print df
# slice time and acceleration columns for plotting ground motion time history
#time=df.loc[:,"time"]
acc2=df2.loc[:,"acc2"] 

# Read first vel. file in pandas and set column names
f3=open('/home/mmiah/Documents/investigate/new_plots/m7/S_07_17/velspec','r')
df3 = pd.read_csv(f3, sep="\s+", header=3, names=['time','vel1'])
# slice time and acceleration columns for plotting ground motion time history
vel1=df3.loc[:,"vel1"] 

# Read second vel. file in pandas and set column names
f4=open('/home/mmiah/Documents/investigate/new_plots/m65/S_07_22/velspec','r')
df4 = pd.read_csv(f4, sep="\s+", header=3, names=['time','vel2'])
# slice time and acceleration columns for plotting ground motion time history
time=df4.loc[:,"time"]
vel2=df4.loc[:,"vel2"] 

## plot and overlay acceleration spectra for two events
plt.subplot(1,2,1)
plt.grid(True)
plt.plot(time, acc1*39.37,linewidth=7, label="M=7.0", color='red')
plt.plot(time, acc2*39.37,linewidth=7, label="M=6.5", color='blue')

plt.xlabel('Period (seconds)', fontsize=50,fontname="Times New Roman Bold")
plt.ylabel('Spectral acceleration (in/s2)', fontsize=50,fontname="Times New Roman Bold")
plt.legend(fontsize=50)
plt.ylim(0,520)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=10)
## plot and overlay velocity spectra for two events
plt.subplot(1,2,2)
plt.grid(True)
plt.plot(time, vel1*39.37,linewidth=7, label="M=7.0", color='red')
plt.plot(time, vel2*39.37,linewidth=7, label="M=6.5", color='blue')
## Read disp. file in pandas and set column names
#f=open('dispspec','r')
#df = pd.read_csv(f, sep="\s+", header=3, names=['time','disp'])
##print df
## slice time and acceleration columns for plotting ground motion time history
#time=df.loc[:,"time"]
#disp=df.loc[:,"disp"] 
#plt.plot(time, disp,linewidth=2.5, label="Displacement")

#disp=integrate.cumtrapz(velocity,time,initial=0)
#print disp
#plt.plot(time, disp*39.37, linewidth=2.5, color='green', label="Displacement")
#plt.title('S_14_20 (4 km away)',fontsize=40,fontname="Times New Roman Bold", y=1.05)
plt.xlabel('Period (seconds)', fontsize=50,fontname="Times New Roman Bold")
plt.ylabel('Spectral velocity (in/s)', fontsize=50,fontname="Times New Roman Bold")
plt.legend(fontsize=50)
plt.ylim(0,90)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=10)
plt.savefig('accspec-S_14_20.pdf')
plt.show()
