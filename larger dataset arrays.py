# creating two datasets to play with
import numpy as np
height = np.round(np.random.normal(1.75,0.20,5000),2)
weight = np.round(np.random.normal(60.32,15,5000),2)
np_city = np.column_stack((height, weight))

# print out data
# the average height of the people in the array
print(np.mean(height))
print(np.mean(np_city[:,0]))
# the median, the height of the middle person standing in a height ordered line
print(np.median(np_city[:,0]))

# find any correlation between the two lists
np_corr = np.corrcoef(np_city[:,0], np_city[:,1])
print(np_corr)
# standard deviation
print(np.std(np_city[:,0]))
