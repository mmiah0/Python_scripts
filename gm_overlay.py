## python script for plotting ground acceleration, velocity, and displacement

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 25, 17
style.use('ggplot')

# Read first file in pandas and set column names
f=open('/home/mmiah/Documents/investigate/m6.5/S_07_40.data','r')
df = pd.read_csv(f, sep="\s+", header=1, names=['time','accX', 'accY', 'accZ'])
#print df.loc[:, "time"]
# slice time and acceleration columns for plotting ground motion time history
time=df.loc[0:2999,"time"]
acc=df.loc[0:2999,"accX"] # switch labels for normal and parallel components

# Read second file in pandas and set column names
f=open('/home/mmiah/Documents/investigate/m7/S_07_40.data','r')
df = pd.read_csv(f, sep="\s+", header=1, names=['time','accX', 'accY', 'accZ'])
time2=df.loc[0:2999,"time"]
acc2=df.loc[0:2999,"accX"] # switch labels for normal and parallel components

# Integration of acceleration data to plot velocity time history
import scipy
from scipy import integrate
vel=integrate.cumtrapz(acc,time,initial=0)
vel2=integrate.cumtrapz(acc2,time2,initial=0)

# Integration of velocity data to plot displacement time history
disp=integrate.cumtrapz(vel,time,initial=0)
disp2=integrate.cumtrapz(vel2,time2,initial=0)

# Write acceleration, velocity, and displacement data to a file
f1=open("/home/mmiah/Documents/investigate/m6.5/M6.5-S_14_80.txt", "w")
f2=open("/home/mmiah/Documents/investigate/m7/M7.0-S_14_80.txt", "w")
f1.write("# Columns represent time(s), acceleration(in/s2), velocity(in/s), and displacement(in) respectively"+'\n')
for item in zip(time, acc, vel, disp):
  val='   '.join(map(str,item))
  f1.write(str(val).strip("()")+'\n')
  
plt.subplot(2,1,1)
plt.plot(time, acc*39.37,linewidth=2.5, label="Acceleration")
plt.plot(time, vel*39.37, linewidth=2.5, color='blue', label="Velocity")
plt.plot(time, disp*39.37, linewidth=2.5, color='green', label="Displacement")

plt.title('M6.5 (S_14_80-FN)',fontsize=40,fontname="Times New Roman Bold", y=0.85)
plt.ylabel('Ground motion (in/s2, in/s, in)', fontsize=35,fontname="Times New Roman Bold", y=0)
plt.legend(fontsize=35)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)

plt.subplot(2,1,2)
plt.plot(time2, acc2*39.37,linewidth=2.5)
plt.plot(time2, vel2*39.37, linewidth=2.5, color='blue')
plt.plot(time2, disp2*39.37, linewidth=2.5, color='green')
plt.title('M7.0',fontsize=40,fontname="Times New Roman Bold", y=0.85)
plt.xlabel('Time (seconds)', fontsize=35,fontname="Times New Roman Bold")

plt.legend(fontsize=35)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.savefig('S_14_80.pdf')

plt.show()
