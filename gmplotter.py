## python script for plotting ground acceleration, velocity, and displacement

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 25, 25

# Read file in pandas and set column names
f=open('S_11_55.data','r')
df = pd.read_csv(f, sep="\s+", header=1, names=['time','accX', 'accY', 'accZ'])
#print df
plt.subplot(3,1,1)
# slice time and acceleration columns for plotting ground motion time history
time=df.loc[:,"time"]
acc=df.loc[:,"accX"] # switch labels for normal and parallel components
plt.plot(time, acc/9.8,linewidth=3.5, color = 'red', label="Acceleration (g)")
#plt.title('Ground motion time history at S_11_55 (FP)',fontsize=50,fontname="Times New Roman Bold", y = 1.09)
#plt.xlabel('Time (seconds)', fontsize=30,fontname="Times New Roman Bold")
#plt.ylabel('Acc. (g)', fontsize=70,fontname="Times New Roman Bold")
plt.legend(fontsize=80)
#plt.xticks(fontsize=80)
plt.yticks(fontsize=80)
plt.ylim(-1,1)
ax=plt.gca()
ax.tick_params(axis='both', which='major', labelbottom =False, pad=18)
plt.tight_layout()
#plt.show()

# Integration of acceleration data to plot velocity time history
import scipy
from scipy import integrate
velocity=integrate.cumtrapz(acc,time,initial=0)
print velocity
plt.subplot(3,1,2)
plt.plot(time, velocity, linewidth=4.5, color='green', label="Velocity (m/s)")
#plt.title('Velocity time history (3st_S_01_30_ns)',fontsize=20,fontname="Times New Roman Bold")
#plt.xlabel('Time (seconds)', fontsize=30,fontname="Times New Roman Bold")
#plt.ylabel('Vel. (m/s)', fontsize=50,fontname="Times New Roman Bold")
plt.legend(fontsize=80)
#plt.xticks(fontsize=80)
plt.yticks(fontsize=80)
plt.ylim(-1,1)
ax=plt.gca()
ax.tick_params(axis='both', which='major', labelbottom =False, pad=18)
plt.tight_layout()
#plt.show()

# Integration of velocity data to plot displacement time history

disp=integrate.cumtrapz(velocity,time,initial=0)
print disp
plt.subplot(3,1,3)
plt.plot(time, disp, linewidth=4.5, color='blue', label="Displacement (m)")
#plt.title('Ground displacement at S_06_26',fontsize=50,fontname="Times New Roman Bold", y=1.05)
plt.xlabel('Time (seconds)', fontsize=80,fontname="Times New Roman Bold")
#plt.ylabel('Disp. (m)', fontsize=50,fontname="Times New Roman Bold")
plt.legend(fontsize=80, loc=0)
plt.xticks(fontsize=80)
plt.yticks(fontsize=80)
plt.ylim(-0.75,0.75)
plt.tight_layout()
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=18)
plt.savefig('S_11_55_fp_motions.pdf')
plt.show()
