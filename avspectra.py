## python script for plotting ground acceleration, velocity, and displacement

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 19, 25
from pylab import *
rc('axes', linewidth=5)
#style.use('ggplot')

# Read vel. file in pandas and set column names
f=open('/Users/MMiah/Documents/artie/hf_m7_4runs/HF_M7.0_3DTOPO_H50MR/data/S_22_20/accspec','r')
df = pd.read_csv(f, sep="\s+", header=3, names=['time','acc'])
#print df
# slice time and acceleration columns for plotting ground motion time history
time=df.loc[:,"time"]
acc=df.loc[:,"acc"] 
plt.subplot(3,1,1)
plt.grid(True)
plt.title('Fault-normal component', fontsize=50, y = 1.05)
plt.plot(time, acc/9.8,linewidth=5, label="Sa (1.25 Hz)", color='black')
#plt.xlabel('Period (seconds)', fontsize=50,fontname="Times New Roman Bold",labelpad=15)
plt.ylabel('Spectral acc. (g)', fontsize=50,fontname="Times New Roman Bold",labelpad=15)
plt.legend(fontsize=50)
plt.ylim(0,2.0)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.tight_layout()
ax=plt.gca()
ax.tick_params(axis='both', which='major', labelbottom=False, pad=25)
##
# Read vel. file in pandas and set column names
f=open('/Users/MMiah/Documents/artie/hf_m7_4runs/HF_M7.0_3DTOPO_H50MR/data/S_22_20/velspec','r')
df = pd.read_csv(f, sep="\s+", header=3, names=['time','vel'])
#print df
# slice time and acceleration columns for plotting ground motion time history
time=df.loc[:,"time"]
vel=df.loc[:,"vel"] 
plt.subplot(3,1,2)
plt.grid(True)
#plt.title('S_11_45', fontsize=50, y = 1.05)
plt.plot(time, vel,linewidth=5, label="Sv", color='black')
#plt.xlabel('Period (seconds)', fontsize=50,fontname="Times New Roman Bold",labelpad=15)
plt.ylabel('Spectral vel. (m/s)', fontsize=50,fontname="Times New Roman Bold",labelpad=15)
plt.legend(fontsize=50)
plt.ylim(0,1)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.tight_layout()
ax=plt.gca()
ax.tick_params(axis='both', which='major', labelbottom=False, pad=25)

# plot displacement spectra
f=open('/Users/MMiah/Documents/artie/hf_m7_4runs/HF_M7.0_3DTOPO_H50MR/data/S_22_20/dispspec','r')
df = pd.read_csv(f, sep="\s+", header=3, names=['time','disp'])
#print df
# slice time and acceleration columns for plotting ground motion time history
time=df.loc[:,"time"]
dis=df.loc[:,"disp"] 
plt.subplot(3,1,3)
plt.grid(True)
plt.plot(time, dis,linewidth=5, label="Sd", color='black')
plt.xlabel('Period (seconds)', fontsize=50,fontname="Times New Roman Bold",labelpad=15)
plt.ylabel('Spectral disp. (m)', fontsize=50,fontname="Times New Roman Bold",labelpad=15)
plt.legend(fontsize=50, loc='lower right')
plt.ylim(0,.5)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=25)
plt.tight_layout()
plt.savefig('1.25_Hz_fn_spec.pdf')
plt.show()
