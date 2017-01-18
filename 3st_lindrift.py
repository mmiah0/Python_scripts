#!/usr/bin/env python
# python script to compute interstory drift from NEVADA output
# This script is based on 3 story NONLINEAR frame model
# Node numbers need to be adjusted for the output of interest
# For other building models additional srcipts will be needed.

import numpy as np

f=open('output','r')
#lines=f.readlines()
second = []
third = []
roof = []
drift1=[]
drift2=[]
drift3=[]
#print lines[10]
for line in f:
  if line.startswith('        11'):  # for linear change it to 11
    second.append(float(line[21:33]))
  if line.startswith('        16'):  # for linear change it to 16
    third.append(float(line[21:33]))
  if line.startswith('        21'):  # for linear change it to 21
    roof.append(float(line[21:33]))

for i in range(0,len(second)):
  drift1.append(second[i]-0)
  drift2.append(third[i]-second[i])
  drift3.append(roof[i]-third[i])

#print drift2

# The following scripts save the roof displacements to a file named 'roofdisp.txt'
import csv
with open('roofdisp.txt','w') as f:
  writer = csv.writer(f)
  for item in roof:
    writer.writerow([item])

# The following scripts save the drift histories to a file named 'storydrift'
with open('storydrift','w') as f:
#  writer = csv.writer(f)
  for val in zip(drift1, drift2, drift3):
    f.write(str(val).strip("()")+'\n')

# The following scripts print the maximum drifts of all three floors across the entire time span
maxdrift1 =  max(abs(max(drift1)), abs(min(drift1)))
maxdrift2 =  max(abs(max(drift2)), abs(min(drift2)))
maxdrift3 =  max(abs(max(drift3)), abs(min(drift3)))

#print 'Maximum drift for the 1st floor = ', maxdrift1
#print 'Maximum drift for the 2nd floor = ', maxdrift2
#print 'Maximum drift for the 3rd floor = ', maxdrift3
#
# Compute interstory drift ratios
# story height is 156 inches for 3 story building

#print 'drift for the 1st floor = ', maxdrift1
#print 'drift for the 2nd floor = ', maxdrift2
#print 'drift for the 3rd floor = ', maxdrift3

d1=maxdrift1/156*100  # Height of the first floor is 18 ft
d2=maxdrift2/156*100
d3=maxdrift3/156*100

print 'drift for the 1st floor = ',d1, '%'
print 'drift for the 2nd floor = ',d2, '%'
print 'drift for the 3rd floor = ',d3, '%'

# The following section is for creating time history
## IMPORTANT: Adjust the time increment accordingly
time=[]
count = 0
for i in range (0,len(roof)):
  count += 0.025
  time.append(count)
print len(time)

## scripts below are for plotting purpose alone

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

##
plt.plot(time,roof,linewidth=2.0, color='red')
plt.title('3st_S_37_30_ew_lin',fontsize=16,fontname="Times New Roman Bold")
plt.xlabel('Time, seconds', fontsize=12,fontname="Times New Roman Bold")
plt.ylabel('Roof displacement, inches', fontsize=12,fontname="Times New Roman Bold")
plt.grid(True)
#plt.show()
plt.savefig('foo.pdf')

# Plot bar chart for interstory drifts
drifts=[d1,d2,d3]
N=len(drifts)
story=np.linspace(1,N,N)
#print story
print drifts[1]

from pylab import *
figure(2)
barh(story,drifts,align='center', color='blue', height=0.1)
title('3st_S_37_30_ew_lin')
xlabel('Drift ratio (%)')
ylabel('Story number')
grid(True)
plt.savefig('bar.pdf')


#import subprocess as sp
#args = ["awk", r'{OFS="\t"; print $2,$4,$5,$6}', "B3LYPD.txt"]

#p = sp.Popen(args, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE )
#print(p.stdout.readline()) # will give you the first line of the awk output

#awk '/^       102/' output | awk -F' ' '{print $2}' > roofdisp.txt
