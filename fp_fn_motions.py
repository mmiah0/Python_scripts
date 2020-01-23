## python script for plotting peak interstory drift (PID) vs.
## spectral amplitude at a building's first modal period

import matplotlib.pyplot as plt
from matplotlib import style
from pylab import rcParams
rcParams['figure.figsize'] = 25, 22
#style.use('ggplot')
from pylab import *
rc('axes', linewidth=5)

import pandas as pd
# Read pgv file in pandas and set column names
f1=open('fppgv.txt','r')
df1 = pd.read_csv(f1, sep="\s+", header=0, names=['x','y', 'fppgv'])
fn=df1.loc[:,"fppgv"] # switch labels for normal and parallel components

# Read pgd file in pandas and set column names
f2=open('fppga.txt','r')
df2 = pd.read_csv(f2, sep="\s+", header=0, names=['x','y', 'fppga'])
fp=df2.loc[:,"fppga"]

# Put the pgv and pgd values in bins based on distance away from the fault
# Plotting pgv vs pgd binwise would help understand how they correlate in 
# both near-fault and far-field locations.
fn5=[]
fn10=[]
fn15=[]
fn20=[]
fn25=[]
fn10.append(fn[245:343])
fn15.append(fn[343:490])
fn20.append(fn[490:735])
fn25.append(fn[735:931])

fp5=[]
fp10=[]
fp15=[]
fp20=[]
fp25=[]
fp10.append(fp[245:343])
fp15.append(fp[343:490])
fp20.append(fp[490:735])
fp25.append(fp[735:931])


#print 'length of the drift slices are =', len(ten)
#print 'length of the acc slices are =', len(acc10[0])

## plot PGV vs. PGD to see correlations
#plt.scatter(acc, drift, s=100, linewidth=1.5, label="PGA")
#plt.scatter(acc5[0], five, s=150, color='goldenrod', linewidth=1.5, label="5 km")
plt.scatter(fn10[0], fp10[0], s=175, color='red', linewidth=1.5, label="0-4 km")
plt.scatter(fn15[0], fp15[0], s=175, color='green', linewidth=1.5, label="4-10 km")
plt.scatter(fn20[0], fp20[0], s=175, color='blue', linewidth=1.5, label="10-20 km")
plt.scatter(fn25[0], fp25[0], s=175, color='black', linewidth=1.5, label="> 20 km")
#plt.scatter(acc29[0], twenty9, s=150, color='black', linewidth=1.5, label=">30 km")

plt.xlim(xmin=0)
plt.ylim(ymin=0)
plt.title('PGV vs. PGA motions (5 Hz, FP)',fontsize=60,fontname="Times New Roman Bold", y=1.05)
plt.xlabel('Fault-parallel PGA (m/s2)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.ylabel('Fault-parallel PGV (m/s)', fontsize=60,fontname="Times New Roman Bold", labelpad=30)
plt.xticks(fontsize=50)
plt.yticks(fontsize=50)
plt.legend(fontsize=50, loc = 'upper left')
ax=plt.gca()
ax.tick_params(axis='both', which='major', pad=18)
plt.grid(True, linewidth=2)
plt.show()
