import matplotlib.pyplot as plt
import numpy as np

'''
#Plotting Histogram
y = np.random.randn(100,100)    #100 X 100 array of a guassian distribution
plt.hist(y)
plt.show()


#Plotting a Dict. using Bar Chart
d = {'a':25, 'b':45, 'c':52}
for i, key in enumerate(d):
    plt.bar(i, d[key])

plt.xticks(np.arange(len(d)), d.keys())    #adding the keys as label on x-axis
plt.show()


#Plooting Pie Chart
plt.figure(figsize= (3,3))    #size of the plot in inches
plt.pie([40, 24, 5], labels=['Python', 'Java', 'C++'])
plt.show()
'''

#Scatter Plot
x = np.random.randn(200)
y = np.random.randn(200)
plt.scatter(x, y)
plt.show()