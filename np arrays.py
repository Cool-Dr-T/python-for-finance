import numpy as np
# creating 2 1D arrays with data
np_height = np.array([1.73,1.68,1.71,1.89,1.79])
np_weight = np.array([65.4,59.2,63.6,88.4,68.7])
# printing the type of array
print(type(np_height))
print(type(np_weight))

# now working with 2D arrays
np_2d = np.array([[1.73,1.68,1.71,1.89,1.79],[65.4,59.2,63.6,88.4,68.7]])
print(np_2d)
# shape gives the dimensions of the array
print(np_2d.shape)
# np arrays can only contain one datatype, if one value is changed (e.g. '68.7'
# then all the values will be converted to strings

print('printing np_2d[0] - prints the first row')
print(np_2d[0])

print('printing np_2d[0][2] - will give the 2th value in the 0th list')
print(np_2d[0][2])

print('printing np_2d[0,2] - same as above')
print(np_2d[0,2])

# we can get a subset of the values in the list
print(np_2d[:,1:3])
# this gives a 2d array with 2 rows and 2 columns
# the colon gives both (all) rows and the 1th and 2th column in those rows
# the 3th column is not included as the last reference is the 'upto' value

# if I want to select the weight of all family members
# that is all the columns in the second row
print(np_2d[1,:])
