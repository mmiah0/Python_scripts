## python script for plotting PGA vs peak interstory drift
import numpy as np
import scipy
from scipy import stats
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 25, 22
#style.use('ggplot')
from pylab import *
rc('axes', linewidth=5)

# Read and manipulate PGA and drift files to map their pairs
# and write to a file
#f=open('driftvsjerk.txt','w')
with open('normalpga.txt','r') as f1, open('40st_m7_fn_drift.txt', 'r') as f2:
 acc=[]
 drift=[]
 five=[]
 ten=[]
 twenty=[]
 thirty=[]
 forty=[]
 twenty9=[]
 acc5=[]
 acc10=[] 
 acc20=[] 
 acc30=[] 
 acc40=[] 
 acc29=[] 

 for line1,line2 in zip(f1,f2):
   acc.append((float(line1.split()[1])*39.39))
   drift.append(float(line2.split()[2]))

## Slice the entire region based on some distance away from the fault.
## e.g., if distance is <= 5 km, then that slice of the region will
## contain area up to 5 km from the fault. However, if the stations are
## sampled to every 2 km then that slice would be 5*2=10 km from the fault.

   if float(line2.split()[1]) <= 05:
     five.append(float(line2.split()[2]))
#     acc5.append(float(line1.split()[1][0:194])*39.39)
   if float(line2.split()[1]) > 05 and float(line2.split()[1]) <= 10:
     ten.append(float(line2.split()[2]))
   if float(line2.split()[1]) > 10 and float(line2.split()[1]) <= 15:
     twenty.append(float(line2.split()[2]))
   if float(line2.split()[1]) > 15 and float(line2.split()[1]) <= 20:
     thirty.append(float(line2.split()[2]))
   if float(line2.split()[1]) > 20 and float(line2.split()[1]) <= 25:
     forty.append(float(line2.split()[2]))
   if float(line2.split()[1]) > 25 and float(line2.split()[1]) <= 29:
     twenty9.append(line2.split()[2])

# for item in zip(acc,drift):
#   val='     '.join(map(str,item))
#   f.write(str(val).strip("()")+'\n')

acc5.append(acc[0:245])
acc10.append(acc[245:490])
acc20.append(acc[490:735])
acc30.append(acc[735:980])
acc40.append(acc[980:1176])
#acc29.append(acc[975:1131])


print 'length of the drift slices is =', len(ten)
print 'length of the acc slices is =', len(acc10[0])
## plot PGA vs. drift data to see correlations
#plt.scatter(acc, drift, s=100, linewidth=1.5, label="PGA")
#plt.scatter(acc5[0], five, s=150, color='goldenrod', linewidth=1.5, label="0-10 km, opposite side")
plt.scatter(acc10[0], ten, s=175, color='red', linewidth=1.5, label="0-10 km")
#plt.scatter(acc20[0], twenty, s=175, color='green', linewidth=1.5, label="10-20 km")
#plt.scatter(acc30[0], thirty, s=175, color='blue', linewidth=1.5, label="20-30 km")
#plt.scatter(acc40[0], forty, s=175, color='cyan', linewidth=1.5, label="30-40 km")
#plt.scatter(acc29[0], twenty9, s=150, color='black', linewidth=1.5, label="25 km")

plt.xlim(xmin=0, xmax=100)
plt.ylim(ymin=0)
plt.title('Peak drift vs. PGA for 40 story M7 FN',fontsize=60,fontname="Times New Roman Bold", y=1.05)
plt.xlabel('Peak ground velocity (in/s)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.ylabel('Peak drift (%)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=18)
plt.grid(True, linewidth=2)
plt.legend(fontsize=50)

### Perform linear regression on the scattered data
from numpy import array
x = array(acc)
y = array(drift)
#print x
#print y
#r = scipy.stats.stats.pearsonr(x,y)
#print ('linear correlation: ', r)

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
#print('scipy output:')
#print('intercept: ', intercept)
#print('slope: ', slope)
#print('std_err: ', std_err)
#print ('r :', r_value)

##plt.scatter(x,y, marker='o', s=10, c='b')
xx = np.linspace(x.min(), x.max())
#plt.plot(xx, intercept + slope*xx, ls='-', c='black', lw=5, label='r = %s'%round(r_value, 3))
plt.legend(fontsize=50)
#plt.savefig('Reg-3st-m6.5-FN-pga-5km.pdf')
plt.show()





