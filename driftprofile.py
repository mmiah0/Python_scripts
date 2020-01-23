## python script for plotting structural drift profiles from certain
## distance of a fault

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
#style.use('ggplot')
from pylab import rc, rcParams
rcParams['figure.figsize'] = 25, 17
from pylab import *
rc('axes', linewidth=5)

# Read file in pandas and set column names
f=open('com.txt','r')
df = pd.read_csv(f, sep="\s+", names=['x','y', 'drift'])
#print df
xrange=df.loc[:,'x'] # Store first column as x values
yrange = df.loc[:,'y'] # Store second column as y values
drift=df.loc[:,'drift'] # Store third column as drift values

print yrange[158]
xdist=[]
ydsit=[]
risk=[]

for i in range(max(yrange)+1):
  for j in range(max(xrange)):
    if i == 11:       ## Change i value to plot drift profiles for different slices
      slice=i
      xdist.append(xrange[(i-1)*99+j])  ## There are j=1,2,...,99 stations along the horizontal axis
      risk.append(drift[(i-1)*99+j])

print 'Max PID is ', max(risk)
## For HF use the following block of code
#for i in range(max(xrange)):
#  for j in range(max(yrange)):
#    if i ==15:       ## Change i value to plot drift profiles for different slices
#      slice=i
#      xdist.append(yrange[(i-1)*59+j]*2)  ## There are j=1,2,...,59 stations along the horizontal axis
#      risk.append(drift[(i-1)*59+j])

### save data to a file 
#f=open('20km_3st_fp_c.txt','w')
#for item in zip(xdist[18:81],risk[18:81]):
#  val='     '.join(map(str,item))
#  f.write(str(val).strip("()")+'\n')

plt.plot(xdist, risk,linewidth=7.5, label="20 km from fault (9-story FP)")
#plt.title('Drift variation for 3-story FP motions', fontsize=80,fontname="Times New Roman", fontweight='bold', y=1.06)
plt.xlabel('Locations along fault (km)', fontsize=80,fontname="Times New Roman", fontweight='bold',labelpad=15)
plt.ylabel('Peak interstory drift (%)', fontsize=80,fontname="Times New Roman", fontweight='bold', labelpad=30)
plt.xticks(fontsize=80)
plt.yticks(fontsize=80)
plt.legend(fontsize=40, loc = 'best')
plt.xlim(19,81)
plt.ylim(0,6)
plt.grid(True)
plt.tight_layout()
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=20)
#plt.gca().set_ylim(top=2.0)
plt.savefig('copy1km.pdf')
plt.show()

