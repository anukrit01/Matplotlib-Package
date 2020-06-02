import matplotlib.pyplot as plt
import numpy as np

'''
#Colour Control
y = np.arange(1,3)
plt.plot(y+1, 'y')      #y- yellow
plt.plot(y+3, 'w')      #w- white
plt.plot(y+5, 'm')      #m- magenta
plt.plot(y+7, 'r')      #r- red
plt.plot(y+9, 'k')      #k- black
plt.plot(y+11, 'c')     #c- cyan
plt.plot(y+13, 'g')     #g- green
plt.plot(y+15, 'b')     #b- blue
plt.show()


#Control Line Styling
y = np.arange(1, 100)
plt.plot(y, '--', y*5, '-.', y*10, ':')
plt.show()
'''

#Control Marker Styling
y = np.arange(1, 10, 0.5)
plt.plot(y, '*', y+5, 'o', y+10, 'D', y+2, '^', y+3, 's')
plt.show()