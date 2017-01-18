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

twenty1=[]
twenty2=[]
twenty3=[]
twenty4=[]
twenty5=[]
twenty6=[]
twenty7=[]
twenty8=[]
twenty9=[]
thirty=[]

thirty1=[]
thirty2=[]
thirty3=[]
thirty4=[]
thirty5=[]
thirty6=[]
thirty7=[]
thirty8=[]
thirty9=[]
forty=[]

#print lines[10]
for line in f:
  if line.startswith('       225'):
    one.append(float(line[21:33]))
  if line.startswith('       280'):
    two.append(float(line[21:33]))
  if line.startswith('       335'):
    three.append(float(line[21:33]))
  if line.startswith('       390'):
    four.append(float(line[21:33]))
  if line.startswith('       445'):
    five.append(float(line[21:33]))
  if line.startswith('       500'):
    six.append(float(line[21:33]))
  if line.startswith('       555'):
    seven.append(float(line[21:33]))
  if line.startswith('       610'):
    eight.append(float(line[21:33]))
  if line.startswith('       665'):
    nine.append(float(line[21:33]))
  if line.startswith('       720'):
    ten.append(float(line[21:33]))

  if line.startswith('       775'):
    eleven.append(float(line[21:33]))
  if line.startswith('       830'):
    twelve.append(float(line[21:33]))
  if line.startswith('       885'):
    thirteen.append(float(line[21:33]))
  if line.startswith('       940'):
    fourteen.append(float(line[21:33]))
  if line.startswith('       995'):
    fifteen.append(float(line[21:33]))
  if line.startswith('      1050'):
    sixteen.append(float(line[21:33]))
  if line.startswith('      1105'):
    seventeen.append(float(line[21:33]))
  if line.startswith('      1160'):
    eighteen.append(float(line[21:33]))
  if line.startswith('      1215'):
    nineteen.append(float(line[21:33]))
  if line.startswith('      1270'):
    twenty.append(float(line[21:33]))

  if line.startswith('      1325'):
    twenty1.append(float(line[21:33]))
  if line.startswith('      1380'):
    twenty2.append(float(line[21:33]))
  if line.startswith('      1435'):
    twenty3.append(float(line[21:33]))
  if line.startswith('      1490'):
    twenty4.append(float(line[21:33]))
  if line.startswith('      1545'):
    twenty5.append(float(line[21:33]))
  if line.startswith('      1600'):
    twenty6.append(float(line[21:33]))
  if line.startswith('      1655'):
    twenty7.append(float(line[21:33]))
  if line.startswith('      1710'):
    twenty8.append(float(line[21:33]))
  if line.startswith('      1765'):
    twenty9.append(float(line[21:33]))
  if line.startswith('      1820'):
    thirty.append(float(line[21:33]))

  if line.startswith('      1875'):
    thirty1.append(float(line[21:33]))
  if line.startswith('      1930'):
    thirty2.append(float(line[21:33]))
  if line.startswith('      1985'):
    thirty3.append(float(line[21:33]))
  if line.startswith('      2040'):
    thirty4.append(float(line[21:33]))
  if line.startswith('      2095'):
    thirty5.append(float(line[21:33]))
  if line.startswith('      2150'):
    thirty6.append(float(line[21:33]))
  if line.startswith('      2205'):
    thirty7.append(float(line[21:33]))
  if line.startswith('      2260'):
    thirty8.append(float(line[21:33]))
  if line.startswith('      2315'):
    thirty9.append(float(line[21:33]))
  if line.startswith('      2370'):
    forty.append(float(line[21:33]))

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

drift21 = []
drift22 = []
drift23 =[]
drift24=[]
drift25=[]
drift26 = []
drift27 = []
drift28 =[]
drift29=[]
drift30=[]

drift31 = []
drift32 = []
drift33 =[]
drift34=[]
drift35=[]
drift36 = []
drift37 = []
drift38 =[]
drift39=[]
drift40=[]

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

  drift21.append(twenty1[i]-twenty[i])
  drift22.append(twenty2[i]-twenty1[i])
  drift23.append(twenty3[i]-twenty2[i])
  drift24.append(twenty4[i]-twenty3[i])
  drift25.append(twenty5[i]-twenty4[i])
  drift26.append(twenty6[i]-twenty5[i])
  drift27.append(twenty7[i]-twenty6[i])
  drift28.append(twenty8[i]-twenty7[i])
  drift29.append(twenty9[i]-twenty8[i])
  drift30.append(thirty[i]-twenty9[i])

  drift31.append(thirty1[i]-thirty[i])
  drift32.append(thirty2[i]-thirty1[i])
  drift33.append(thirty3[i]-thirty2[i])
  drift34.append(thirty4[i]-thirty3[i])
  drift35.append(thirty5[i]-thirty4[i])
  drift36.append(thirty6[i]-thirty5[i])
  drift37.append(thirty7[i]-thirty6[i])
  drift38.append(thirty8[i]-thirty7[i])
  drift39.append(thirty9[i]-thirty8[i])
  drift40.append(forty[i]-thirty9[i])

#print drift2

# The following scripts save the roof displacements to a file named 'roofdisp.txt'
import csv
with open('roofdisp.txt','w') as f:
  writer = csv.writer(f)
  for item in forty:
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

maxdrift21 =  max(abs(max(drift21)), abs(min(drift21)))
maxdrift22 =  max(abs(max(drift22)), abs(min(drift22)))
maxdrift23 =  max(abs(max(drift23)), abs(min(drift23)))
maxdrift24 =  max(abs(max(drift24)), abs(min(drift24)))
maxdrift25 =  max(abs(max(drift25)), abs(min(drift25)))
maxdrift26 =  max(abs(max(drift26)), abs(min(drift26)))
maxdrift27 =  max(abs(max(drift27)), abs(min(drift27)))
maxdrift28 =  max(abs(max(drift28)), abs(min(drift28)))
maxdrift29 =  max(abs(max(drift29)), abs(min(drift29)))
maxdrift30 =  max(abs(max(drift30)), abs(min(drift30)))

maxdrift31 =  max(abs(max(drift31)), abs(min(drift31)))
maxdrift32 =  max(abs(max(drift32)), abs(min(drift32)))
maxdrift33 =  max(abs(max(drift33)), abs(min(drift33)))
maxdrift34 =  max(abs(max(drift34)), abs(min(drift34)))
maxdrift35 =  max(abs(max(drift35)), abs(min(drift35)))
maxdrift36 =  max(abs(max(drift36)), abs(min(drift36)))
maxdrift37 =  max(abs(max(drift37)), abs(min(drift37)))
maxdrift38 =  max(abs(max(drift38)), abs(min(drift38)))
maxdrift39 =  max(abs(max(drift39)), abs(min(drift39)))
maxdrift40 =  max(abs(max(drift40)), abs(min(drift40)))

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

d21=maxdrift21/156*100
d22=maxdrift22/156*100
d23=maxdrift23/156*100
d24=maxdrift24/156*100
d25=maxdrift25/156*100
d26=maxdrift26/156*100
d27=maxdrift27/156*100
d28=maxdrift28/156*100
d29=maxdrift29/156*100
d30=maxdrift30/156*100

d31=maxdrift31/156*100
d32=maxdrift32/156*100
d33=maxdrift33/156*100
d34=maxdrift34/156*100
d35=maxdrift35/156*100
d36=maxdrift36/156*100
d37=maxdrift37/156*100
d38=maxdrift38/156*100
d39=maxdrift39/156*100
d40=maxdrift40/216*100

print 'drift for the 1st floor = ',d1, '%'
print 'drift for the 2nd floor = ',d2, '%'
print 'drift for the 3rd floor = ',d3, '%'

# The following section is for creating time history
## IMPORTANT: Adjust the time increment accordingly
time=[]
count = 0
for i in range (0,len(forty)):
  count += 0.02
  time.append(count)
#print time

## scripts below are for plotting purpose alone

import matplotlib.pyplot as plt

# Plot bar chart for interstory drifts
drifts=[d1,d2,d3,d4,d5,d6,d7,d8,d9,d10,d11,d12,d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25,d26,d27,d28,d29,d30,d31,d32,d33,d34,d35,d36,d37,d38,d39,d40]
maxdrift=max(drifts)
print maxdrift
N=len(drifts)
story=np.linspace(1,N,N)
#print story
#print drifts[1]

####################################################################
## write maximum drift in each step to a file called maxdrifts.txt
#f=open('maxdrifts.txt','w')
#for item in zip(story,drifts):
#  f.write(str(item).strip("()")+'\n')

#from pylab import *
#plt.subplot(2,2,1)
#plt.barh(story,drifts,align='center', color='blue', height=0.1)
#plt.title('40st_S_15_23',fontsize=10)
#plt.xlabel('Drift ratio (%)',fontsize=10)
#plt.ylabel('Story number',fontsize=10)
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#grid(True)
##plt.savefig('bar.pdf')

##from matplotlib import style
##style.use('ggplot')

##
##figure(2)
#plt.subplot(2,2,2)
#plt.plot(time,forty,linewidth=1.0, color='red')
##plt.title('40st_S_15_27',fontsize=10,fontname="Times New Roman Bold")
#plt.xlabel('Time, seconds', fontsize=10,fontname="Times New Roman Bold")
#plt.ylabel('Roof displacement, inches', fontsize=10,fontname="Times New Roman Bold")
#plt.xticks(fontsize=8)
#plt.yticks(fontsize=8)
#plt.grid(True)

##plt.show()
#plt.savefig('foo.pdf')
###########################################################################
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
f=open('/home/mmiah/Documents/mapping/'+cwd+'.txt','w')
f.write(locy +' '+ locx+' '+str(maxdrift)+'\n')

#import subprocess as sp
#args = ["awk", r'{OFS="\t"; print $2,$4,$5,$6}', "B3LYPD.txt"]

#p = sp.Popen(args, stdin = sp.PIPE, stdout = sp.PIPE, stderr = sp.PIPE )
#print(p.stdout.readline()) # will give you the first line of the awk output

#awk '/^       102/' output | awk -F' ' '{print $2}' > roofdisp.txt
