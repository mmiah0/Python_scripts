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

#print lines[10]
for line in f:
  if line.startswith('        87'):
    one.append(float(line[21:33]))
  if line.startswith('       127'):
    two.append(float(line[21:33]))
  if line.startswith('       167'):
    three.append(float(line[21:33]))
  if line.startswith('       207'):
    four.append(float(line[21:33]))
  if line.startswith('       247'):
    five.append(float(line[21:33]))
  if line.startswith('       287'):
    six.append(float(line[21:33]))
  if line.startswith('       327'):
    seven.append(float(line[21:33]))
  if line.startswith('       367'):
    eight.append(float(line[21:33]))
  if line.startswith('       407'):
    nine.append(float(line[21:33]))

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

#print drift2

## The following scripts save the roof displacements to a file named 'roofdisp.txt'
#import csv
#with open('roofdisp.txt','w') as f:
#  writer = csv.writer(f)
#  for item in nine:
#    writer.writerow([item])

## The following scripts save the drift histories to a file named 'storydrift'
#with open('storydrift.txt','w') as f:
##  writer = csv.writer(f)
#  for val in zip(drift1, drift2, drift3):
#    f.write(str(val).strip("()")+'\n')

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

print 'drift for the 1st floor = ',d1, '%'
print 'drift for the 2nd floor = ',d2, '%'
print 'drift for the 3rd floor = ',d3, '%'

# The following section is for creating time history
## IMPORTANT: Adjust the time increment accordingly
time=[]
count = 0
for i in range (0,len(nine)):
  count += 0.02
  time.append(count)
#print time

## scripts below are for plotting purpose alone

import matplotlib.pyplot as plt
# Plot bar chart for interstory drifts
drifts=[d1,d2,d3,d4,d5,d6,d7,d8,d9]
maxdrift=max(drifts)
print maxdrift
N=len(drifts)
story=np.linspace(1,N,N)

##
#plt.plot(time,nine,linewidth=2.0, color='red')
#plt.title('9st_S_01_30_ns_nl',fontsize=16,fontname="Times New Roman Bold")
#plt.xlabel('Time, seconds', fontsize=12,fontname="Times New Roman Bold")
#plt.ylabel('Roof displacement, inches', fontsize=12,fontname="Times New Roman Bold")
#plt.grid(True)
##plt.show()
#plt.savefig('foo.pdf')

## Plot bar chart for interstory drifts
#drifts=[d1,d2,d3,d4,d5,d6,d7,d8,d9]
#N=len(drifts)
#story=np.linspace(1,N,N)
##print story
#print drifts[1]

#from pylab import *
#figure(2)
#barh(story,drifts,align='center', color='grey', height=0.1)
#title('S_01_30_ns_nl')
#xlabel('Drift ratio (%)')
#ylabel('Story number')
#grid(True)
#plt.savefig('bar.pdf')

## Combine maxdrift value with the location of the building for contour plot

import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print dir_path
cwd = os.getcwd()[-5:]
locx=cwd[0:2]
locy=cwd[3:5]
#print cwd
#print locx
#print locy
f=open('/home/mmiah/Documents/mapping/9story/fnormal/'+cwd+'.txt','w')
f.write(locy +' '+ locx+' '+str(maxdrift)+'\n')



#import subprocess as sp
#args = ["awk", r'{OFS="\t"; print $2,$4,$5,$6}', "B3LYPD.txt"]

#p = sp.Popen(args, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE )
#print(p.stdout.readline()) # will give you the first line of the awk output

#awk '/^       102/' output | awk -F' ' '{print $2}' > roofdisp.txt
