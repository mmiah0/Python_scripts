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
print 'Number of groundmotions data files is =', len(datafile)

## This block reads each datafile and stores TIME and ACC data
## in two lists
for i in range(0,len(datafile)):
  time=[]
  acc=[]
  for line in open(datafile[i],'r'):
    if not line.startswith('#'):
#  print line.split()[0]
      time.append(float(line.split()[0]))  # corresponds time data
      acc.append(float(line.split()[2])) # corresponds to fault normal motions
#      print acc

## The following block CREATES new directories based on the datafile names
## and copies input file inside
  name = dirs[i]
  filename=os.path.join(name, 'specin')
  if not os.path.exists(os.path.dirname(filename)):
     try:
        os.makedirs(os.path.dirname(filename))
     except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
          raise
  f1= open('/Users/MMiah/Documents/scripts/specheader','r')
  f= open(filename, "w")
  for line in f1:
     f.write(line)
  for val in acc:
     f.write(str(val)+'\n')

#  for val in zip(time,acc):
#     mystring='     '.join(map(str,val))
#     f.write(mystring.strip("()")+'\n')
    

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






