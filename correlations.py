## python script for plotting PGA vs peak interstory drift
import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 27, 23
#style.use('ggplot')
from pylab import *
rc('axes', linewidth=5)

# read and manipulate acceleration and drift files to map their pairs
# and write to a file
with open('fnpgv.txt','r') as f1, open('20st_fn_drift.txt', 'r') as f2:
 acc=[]
 drift=[]
 five=[]
 ten=[]
 fifteen=[]
 twenty=[]
 twenty5=[]
 twenty9=[]
 acc5=[]
 acc10=[] 
 acc15=[] 
 acc20=[] 
 acc25=[] 
 acc29=[] 

 for line1,line2 in zip(f1,f2):
   acc.append(float(line1.split()[2]))
   drift.append(line2.split()[2])

## Slice the entire region based on the distance away from the fault
## e.g., If distance is <= 5 km, then that slice of the region will
## contain area upto 5 km away from the fault. However, if the stations are
## indexed as every 2 km then that slice would be 5*2 = 10 km from fault

   if float(line2.split()[1]) <= 05:
     five.append(line2.split()[2])
#     acc5.append(float(line1.split()[1][0:194])*39.39)
   if float(line2.split()[1]) > 05 and float(line2.split()[1]) <= 07:
     ten.append(line2.split()[2])
   if float(line2.split()[1]) > 07 and float(line2.split()[1]) <= 10:
     fifteen.append(line2.split()[2])
   if float(line2.split()[1]) > 10 and float(line2.split()[1]) <= 15:
     twenty.append(line2.split()[2])
   if float(line2.split()[1]) > 15 and float(line2.split()[1]) <= 20:
     twenty5.append(line2.split()[2])
#   if float(line2.split()[1]) > 20 and float(line2.split()[1]) <= 39:
#     twenty9.append(line2.split()[2])

# for item in zip(acc,drift):
#   val='     '.join(map(str,item))
#   f.write(str(val).strip("()")+'\n')

#acc5.append(acc[0:245])
acc10.append(acc[245:343])
acc15.append(acc[343:490])
acc20.append(acc[490:735])
acc25.append(acc[735:931])
#acc29.append(acc[975:1131])

print 'length of the drift slices are =', len(ten)
print 'length of the acc slices are =', len(acc10[0])
## plot PGA vs. drift data to see correlations
ax=plt.gca()
#plt.scatter(acc, drift, s=100, linewidth=1.5, label="PGA")
#plt.scatter(acc5[0], five, s=150, color='goldenrod', linewidth=1.5, label="5 km")
#ax.scatter(acc10[0], ten, s=175, color='red', linewidth=1.5, label="0-4 km")
#ax.scatter(acc15[0], fifteen, s=175, color='green', linewidth=1.5, label="4-10 km")
#ax.scatter(acc20[0], twenty, s=175, color='blue', linewidth=1.5, label="10-20 km")
ax.scatter(acc25[0], twenty5, s=175, color='black', linewidth=1.5, label="> 20 km")

#ax.set_xscale('log')
#ax.set_yscale('log')
#plt.scatter(acc29[0], twenty9, s=150, color='black', linewidth=1.5, label=">30 km")

plt.xlim(xmin=0, xmax=2)
plt.ylim(ymin=0.1, ymax=3)
plt.title('20-story PID vs. PGV plot for M7.0 (5Hz, FN) motions',fontsize=60,fontname="Times New Roman Bold", y=1.05)
plt.xlabel('Peak ground velocity (m/s)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.ylabel('Peak interstory drift (%)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.legend(fontsize=50, loc = 'lower right')
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=18)
plt.grid(True, linewidth=2)
plt.savefig('20st_fn_drift_pgv_20-30km.pdf')
plt.show()
