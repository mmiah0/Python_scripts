# python script to compute interstory drift from NEVADA output
# This script is based on 3 story NONLINEAR frame model
# Node numbers need to be adjusted for the output of interest
# For other building models additional srcipts will be needed.
#!/usr/bin/env python
import numpy as np

f=open('output','r')

one = []
two = []
three =[]
four=[]
five=[]
six = []
seven = []
eight =[]
nine=[]
ten=[]

eleven = []
twelve = []
thirteen =[]
fourteen=[]
fifteen=[]
sixteen = []
seventeen = []
eighteen =[]
nineteen=[]
twenty=[]


#print lines[10]
for line in f:
  if line.startswith('       124'):
    one.append(float(line[21:33]))
  if line.startswith('       163'):
    two.append(float(line[21:33]))
  if line.startswith('       202'):
    three.append(float(line[21:33]))
  if line.startswith('       241'):
    four.append(float(line[21:33]))
  if line.startswith('       280'):
    five.append(float(line[21:33]))
  if line.startswith('       319'):
    six.append(float(line[21:33]))
  if line.startswith('       358'):
    seven.append(float(line[21:33]))
  if line.startswith('       397'):
    eight.append(float(line[21:33]))
  if line.startswith('       436'):
    nine.append(float(line[21:33]))
  if line.startswith('       475'):
    ten.append(float(line[21:33]))

  if line.startswith('       514'):
    eleven.append(float(line[21:33]))
  if line.startswith('       553'):
    twelve.append(float(line[21:33]))
  if line.startswith('       592'):
    thirteen.append(float(line[21:33]))
  if line.startswith('       631'):
    fourteen.append(float(line[21:33]))
  if line.startswith('       670'):
    fifteen.append(float(line[21:33]))
  if line.startswith('       709'):
    sixteen.append(float(line[21:33]))
  if line.startswith('       748'):
    seventeen.append(float(line[21:33]))
  if line.startswith('       787'):
    eighteen.append(float(line[21:33]))
  if line.startswith('       826'):
    nineteen.append(float(line[21:33]))
  if line.startswith('       865'):
    twenty.append(float(line[21:33]))


# Declare arrays to store interstory drifts
drift1 = []
drift2 = []
drift3 =[]
drift4=[]
drift5=[]
drift6 = []
drift7 = []
drift8 =[]
drift9=[]
drift10=[]

drift11 = []
drift12 = []
drift13 =[]
drift14=[]
drift15=[]
drift16 = []
drift17 = []
drift18 =[]
drift19=[]
drift20=[]


# Following scripts compute drift histories for all the floors
for i in range(0,len(one)):
  drift1.append(one[i])
  drift2.append(two[i]-one[i])
  drift3.append(three[i]-two[i])
  drift4.append(four[i]-three[i])
  drift5.append(five[i]-four[i])
  drift6.append(six[i]-five[i])
  drift7.append(seven[i]-six[i])
  drift8.append(eight[i]-seven[i])
  drift9.append(nine[i]-eight[i])
  drift10.append(ten[i]-nine[i])

  drift11.append(eleven[i]-ten[i])
  drift12.append(twelve[i]-eleven[i])
  drift13.append(thirteen[i]-twelve[i])
  drift14.append(fourteen[i]-thirteen[i])
  drift15.append(fifteen[i]-fourteen[i])
  drift16.append(sixteen[i]-fifteen[i])
  drift17.append(seventeen[i]-sixteen[i])
  drift18.append(eighteen[i]-seventeen[i])
  drift19.append(nineteen[i]-eighteen[i])
  drift20.append(twenty[i]-nineteen[i])

#print drift2

# The following scripts save the roof displacements to a file named 'roofdisp.txt'
import csv
with open('roofdisp.txt','w') as f:
  writer = csv.writer(f)
  for item in twenty:
    writer.writerow([item])

# The following scripts save the drift histories to a file named 'storydrift'
with open('storydrift.txt','w') as f:
#  writer = csv.writer(f)
  for val in zip(drift1, drift2, drift3):
    f.write(str(val).strip("()")+'\n')

# The following scripts print the maximum drifts of all three floors across the entire time span
maxdrift1 =  max(abs(max(drift1)), abs(min(drift1)))
maxdrift2 =  max(abs(max(drift2)), abs(min(drift2)))
maxdrift3 =  max(abs(max(drift3)), abs(min(drift3)))
maxdrift4 =  max(abs(max(drift4)), abs(min(drift4)))
maxdrift5 =  max(abs(max(drift5)), abs(min(drift5)))
maxdrift6 =  max(abs(max(drift6)), abs(min(drift6)))
maxdrift7 =  max(abs(max(drift7)), abs(min(drift7)))
maxdrift8 =  max(abs(max(drift8)), abs(min(drift8)))
maxdrift9 =  max(abs(max(drift9)), abs(min(drift9)))
maxdrift10 =  max(abs(max(drift10)), abs(min(drift10)))

maxdrift11 =  max(abs(max(drift11)), abs(min(drift11)))
maxdrift12 =  max(abs(max(drift12)), abs(min(drift12)))
maxdrift13 =  max(abs(max(drift13)), abs(min(drift13)))
maxdrift14 =  max(abs(max(drift14)), abs(min(drift14)))
maxdrift15 =  max(abs(max(drift15)), abs(min(drift15)))
maxdrift16 =  max(abs(max(drift16)), abs(min(drift16)))
maxdrift17 =  max(abs(max(drift17)), abs(min(drift17)))
maxdrift18 =  max(abs(max(drift18)), abs(min(drift18)))
maxdrift19 =  max(abs(max(drift19)), abs(min(drift19)))
maxdrift20 =  max(abs(max(drift20)), abs(min(drift20)))

#print 'Maximum drift for the 1st floor = ', maxdrift1
#print 'Maximum drift for the 2nd floor = ', maxdrift2
#print 'Maximum drift for the 3rd floor = ', maxdrift3

# Compute interstory drift ratios
# story height is 156 inches for 3 story building

d1=maxdrift1/216*100  # Height of the first floor is 18 ft
d2=maxdrift2/156*100
d3=maxdrift3/156*100
d4=maxdrift4/156*100
d5=maxdrift5/156*100
d6=maxdrift6/156*100
d7=maxdrift7/156*100
d8=maxdrift8/156*100
d9=maxdrift9/156*100
d10=maxdrift10/156*100

d11=maxdrift11/156*100
d12=maxdrift12/156*100
d13=maxdrift13/156*100
d14=maxdrift14/156*100
d15=maxdrift15/156*100
d16=maxdrift16/156*100
d17=maxdrift17/156*100
d18=maxdrift18/156*100
d19=maxdrift19/156*100
d20=maxdrift20/156*100


print 'drift for the 1st floor = ',d1, '%'
print 'drift for the 2nd floor = ',d2, '%'
print 'drift for the 3rd floor = ',d3, '%'

# The following section is for creating time history
## IMPORTANT: Adjust the time increment accordingly
time=[]
count = 0
for i in range (0,len(twenty)):
  count += 0.025
  time.append(count)
#print time

## scripts below are for plotting purpose alone

import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

#
plt.plot(time,twenty,linewidth=2.0, color='red')
plt.title('20st_S_05_30_ns_nl',fontsize=16,fontname="Times New Roman Bold")
plt.xlabel('Time, seconds', fontsize=12,fontname="Times New Roman Bold")
plt.ylabel('Roof displacement, inches', fontsize=12,fontname="Times New Roman Bold")
plt.grid(True)
#plt.show()
plt.savefig('foo.pdf')

# Plot bar chart for interstory drifts
drifts=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20]
N=len(drifts)
story=np.linspace(1,N,N)
#print story
print drifts[1]

from pylab import *
figure(2)
barh(story,drifts,align='center', color='blue', height=0.1)
title('S_05_30_ns_nl')
xlabel('Drift ratio (%)')
ylabel('Story number')
grid(True)
#figure 2
plt.savefig('bar.pdf')


#import subprocess as sp
#args = ["awk", r'{OFS="\t"; print $2,$4,$5,$6}', "B3LYPD.txt"]

#p = sp.Popen(args, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE )
#print(p.stdout.readline()) # will give you the first line of the awk output

#awk '/^       102/' output | awk -F' ' '{print $2}' > roofdisp.txt
