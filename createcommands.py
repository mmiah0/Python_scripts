#! /usr/bin/python
import os
import errno
import glob

# The following command lists all the files present in a directory
filenames=glob.glob('*')

## This block sorts the files and stores the datafiles and
## directories in two lists
datafile=[]
for files in sorted(filenames):
  if files.startswith('S_'):
    datafile.append(files)
print 'Number of groundmotions data files is =', len(datafile)

## This block writes the commands based on the filenames

f=open('nlbatch','w')

mystring1='(cd /$HOME/Documents/newgroundmotions/'
mystring2=' && /$HOME/Documents/scripts/xnevada) &'
for i in range(0,len(datafile)):
  comm1=mystring1+str(datafile[i])
  command=comm1+mystring2
  f.write(command+'\n')




(cd /global/homes/m/mmiah0/gndmotion/asciidata/S_01_01 && /global/u2/m/mmiah0/scripts/xnevada)


