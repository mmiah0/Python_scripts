#plot_node_output.py - Plot all DOF outputs in a subplot for a given node tag
#Import the HDF5 interface for python

import h5py
import matplotlib.pyplot as plt

#Plot all dofs of this file and node
fileName = "NPPModel_DRM_Motion.h5.03.feioutput"
nodeTag = 177
#if h5py.is_hdf5(fileName): #Check if the file is valid
#Open file and get model name, stage name and time vector

f = h5py.File(fileName, "r")
modelName = f['Model_Name'][:]

stageName = f['Stage_Name'][:]
time = f['time'][:]
#Print this info

print "\nOpened file: {} \n".format(fileName)
print "Model Name = ", modelName[0]
print "Stage Name = ", stageName[0]

#Get position, number of DOFS, and coordinates for this node
pos = f['Model/Nodes/Index_to_Generalized_Displacements'][nodeTag]
print pos
ndof = f['Model/Nodes/Number_of_DOFs'][nodeTag]
print ndof
pos_coord = f['Model/Nodes/Index_to_Coordinates'][nodeTag]
print pos_coord
coords = f['Model/Nodes/Coordinates'][pos_coord:(pos_coord+3)]
#Print info
print "Node number {} has {} DOFs and is located at ({}*m, {}*m, {}*m)-\n".format(nodeTag, ndof, coords[0], coords[1], coords[2])

#Get the displacements outputs for this node
u = f['Model/Nodes/Generalized_Displacements'][pos:(pos+ndof), :]
print u
#Create a NDOFx1 subplot for showing the output time series
plt.close("all")
for i in range(ndof):
  plt.subplot(ndof,1,1+i)
  plt.plot(time,u[i,:])
  plt.ylabel("DOF # {}".format(i+1))
plt.xlabel("Time (s)")
plt.show()
