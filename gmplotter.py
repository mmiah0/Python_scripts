## python script for plotting ground acceleration, velocity, and displacement

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

# Read file in pandas and set column names
f=open('S_04_17.data','r')
df = pd.read_csv(f, sep="\s+", header=1, names=['time','accX', 'accY', 'accZ'])
#print df
# slice time and acceleration columns for plotting ground motion time history
time=df.loc[:,"time"]
accX=df.loc[:,"accX"]
plt.plot(time, accX*39.37,linewidth=1.5, label="Acceleration")
#plt.title('3st_S_01_30_ns',fontsize=20,fontname="Times New Roman Bold")
#plt.xlabel('Time (seconds)', fontsize=16,fontname="Times New Roman Bold")
#plt.ylabel('Ground acceleration (in/s2)', fontsize=16,fontname="Times New Roman Bold")

#plt.show()

# Integration of acceleration data to plot velocity time history
import scipy
from scipy import integrate
velocity=integrate.cumtrapz(accX,time,initial=0)
print velocity
plt.plot(time, velocity*39.37, linewidth=1.5, color='blue', label="Velocity")
#plt.title('Velocity time history (3st_S_01_30_ns)',fontsize=20,fontname="Times New Roman Bold")
#plt.xlabel('Time (seconds)', fontsize=16,fontname="Times New Roman Bold")
#plt.ylabel('Ground velocity (in/s)', fontsize=16,fontname="Times New Roman Bold")
#plt.show()

# Integration of velocity data to plot displacement time history

disp=integrate.cumtrapz(velocity,time,initial=0)
print disp
plt.plot(time, disp*39.37, linewidth=1.5, color='green', label="Displacement")
plt.title('Groundmotion time history (S_01_01)',fontsize=20,fontname="Times New Roman Bold")
plt.xlabel('Time (seconds)', fontsize=16,fontname="Times New Roman Bold")
plt.ylabel('Groundmotion (in/s2, in/s, in)', fontsize=16,fontname="Times New Roman Bold")
plt.legend()
plt.savefig('fooX.pdf')
plt.show()
