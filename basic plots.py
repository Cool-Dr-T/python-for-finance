# basic plots with matplotlib
import matplotlib.pyplot as plt
year = [1950,1970,1990,2010]
pop = [2.519,3.692,5.263,6.972]
#plt.scatter(year,pop)

year = [1800,1850,1900] + year
pop = [1.0,1.262,1.650] + pop
plt.plot(year, pop)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World population projections')
plt.yticks([0,2,4,6,8,10],['0','2B','4B','6B','8B','10B'])
# plt.xscale('log') would change the x axis to a log scale
plt.show()
#plt.clf()
#values = [0,0.6,1.4,1.6,2.2,2.5,2.6,3.2,3.5,3.9,4.2,6]
#plt.hist(values, bins = 3)
#plt.show()
