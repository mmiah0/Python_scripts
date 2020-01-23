## python script for plotting PGA vs peak interstory drift
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 25, 25
#style.use('ggplot')
from pylab import *
rc('axes', linewidth=5)

# read and manipulate acceleration and drift files to map their pairs
# and write to a file
with open('3st_fp_drift.txt','r') as f1, open('9st_fp_drift.txt', 'r') as f2:
 fnd=[]
 fpd=[]

 fn5=[]
 fn10=[]
 fn15=[]
 fn20=[]
 fn25=[]
 fn30=[] 

 fp5=[]
 fp10=[]
 fp15=[]
 fp20=[]
 fp25=[]
 fp30=[]

 for line1,line2 in zip(f1,f2):
#   fnd.append(float(line1.split()[1]))
#   fpd.append(line2.split()[1])

#   print float(line2.split()[1])

#   if float(line1.split()[1]) <= 05:
#     fn5.append(float(line1.split()[2]))
#   if float(line2.split()[1]) <= 05:
#     fp5.append(float(line2.split()[2]))

   if float(line1.split()[1]) > 05 and float(line1.split()[1]) <= 07:
     fn10.append(float(line1.split()[2]))
   if float(line2.split()[1]) > 05 and float(line2.split()[1]) <= 07:
     fp10.append(float(line2.split()[2]))

   if float(line1.split()[1]) > 07 and float(line1.split()[1]) <= 10:
     fn15.append(float(line1.split()[2]))
   if float(line2.split()[1]) > 07 and float(line2.split()[1]) <= 10:
     fp15.append(float(line2.split()[2]))

   if float(line1.split()[1]) > 10 and float(line1.split()[1]) <= 15:
     fn20.append(float(line1.split()[2]))
   if float(line2.split()[1]) > 10 and float(line2.split()[1]) <= 15:
     fp20.append(float(line2.split()[2]))

   if float(line1.split()[1]) > 15 and float(line1.split()[1]) <= 20:
     fn25.append(float(line1.split()[2]))
   if float(line2.split()[1]) > 15 and float(line2.split()[1]) <= 20:
     fp25.append(float(line2.split()[2]))

#   if float(line1.split()[1]) > 25 and float(line1.split()[1]) <= 29:
#     fn30.append(float(line1.split()[2]))
#   if float(line2.split()[1]) > 25 and float(line2.split()[1]) <= 29:
#     fp30.append(float(line2.split()[2]))

# for item in zip(acc,drift):
#   val='     '.join(map(str,item))
#   f.write(str(val).strip("()")+'\n')

print len(fn25)
print len(fp25)
print 'Number of fault-normal drifts are =', len(fnd)
print 'Number of fault-parallel drifts are =', len(fpd)
## plot PGA vs. drift data to see correlations
#plt.scatter(fnd, fpd, s=100, linewidth=1.5, label="FN vs. FP")
#plt.scatter(fn5, fp5, s=150, color='goldenrod', linewidth=1.5, label="0 km")
plt.scatter(fn10, fp10, s=150, color='red', linewidth=1.5, label="0-4 km")
plt.scatter(fn15, fp15, s=150, color='green', linewidth=1.5, label="4-10 km")
plt.scatter(fn20, fp20, s=150, color='blue', linewidth=1.5, label="10-20 km")
plt.scatter(fn25, fp25, s=150, color='black', linewidth=1.5, label=">20 km")
#plt.scatter(fn30, fp30, s=150, color='black', linewidth=1.5, label="25 km")

plt.xlim(xmin=0, xmax=3)
plt.ylim(ymin=0, ymax=3)
plt.title('Drift correlation between 3- and 9-story (FP, 5Hz)',fontsize=50,fontname="Times New Roman Bold", y=1.05)
plt.xlabel('3-story drift (%)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.ylabel('9-story drift (%)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.legend(fontsize=50)
plt.grid(True)
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=18)
plt.grid(True, linewidth=2)
#plt.gca().set_yscale('log')
#plt.savefig('3st-m6.5-FN-pgv-5km.pdf')
plt.show()







