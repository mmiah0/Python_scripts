#! /usr/bin/python
import os
import errno
import glob

# The following command lists all the files present in a directory
filenames=glob.glob('*')

## This block sorts the files and stores the datafiles and
## directories in two lists
dirs=[]
datafile=[]
for files in sorted(filenames):
  if files.startswith('S_'):
    dirs.append(files[:-5])
    datafile.append(files)
print 'Number of ground motions data files is =', len(datafile)

## This block reads each datafile and stores TIME and ACC. data
## in two lists
for i in range(0,len(datafile)):
  time=[]
  acc=[]
  for line in open(datafile[i],'r'):
    if not line.startswith('#'):
#  print line.split()[0]
#      time.append(float(line.split()[0]))  # corresponds to time data
      acc.append(float(line.split()[1])) # corresponds to fault normal motions
#      print acc

## Following block of code curtails the record window to eliminate
## the beginning (almost zero shaking) portion of a seismogram
  count=0
  acc2=[]
  for j in range(len(acc)):
    if abs(acc[j]) > .1: # To eliminate really really small acc. values during onset
      k=j                  # that prevents NEVADA from having convergence issues
      break
  
  for item in range(k,len(acc)):
    time.append(count)
    acc2.append(acc[item])
    count = count+0.02  # Change this value if time step changes
#  if abs(acc2[0]-acc2[1]) < 0.01:  # Add criterion to stop choking at the start
#    acc2[1] = acc2[0]+0.1 
#  print acc2[0]
#  print acc2[1]

  time=[len(time)]+time # Adding numer of time steps based on new count
  acc3 = [39.37]+acc2  # Adding meter to in. unit conversion for NEVADA input file

## The following block CREATES new directories based on the datafile names
## and writes input files inside each of these directories
  name = dirs[i]
  filename=os.path.join(name, 'input')
  os.makedirs(os.path.dirname(filename))

  f1= open('9st_nlinput','r')
  f= open(filename, "w")
  for line in f1:
     f.write(line)
  for val in zip(time,acc3):
     mystring='     '.join(map(str,val))
     f.write(mystring.strip("()")+'\n')
    

#for name in dirs:
#  filename=os.path.join(name, 'input')
#  if not os.path.exists(os.path.dirname(filename)):
#    try:
#        os.makedirs(os.path.dirname(filename))
#    except OSError as exc: # Guard against race condition
#        if exc.errno != errno.EEXIST:
#            raise
#  with open(filename, "w") as f:
#    f.write("FOOBAR")



#  if abs(acc[0]-acc[1]) < 0.01:
#    acc[1] = acc[0]+0.1 
#  print acc[0]
#  print acc[1]



