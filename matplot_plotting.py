import matplotlib.pyplot as plt
import numpy as np
'''
plt.plot([1,2,3,4])
plt.show()

#Taking both axises values by user
y_values = [1,2,3,4]
x_values = [i**2 for i in y_values]
print(x_values)
plt.plot(y_values, x_values)
plt.show()


#Multiline plot
x = range(5)
plt.plot(x, [i for i in x], 
            x, [i*i for i in x], 
            x, [i*i*i for i in x])
plt.grid()                          #For showing grid in the background
plt.xlim([0,5])                     #Limiting the X-axis
plt.ylim([0,20])                    #Limiting the Y-axis
plt.xlabel('X-axis')                #Labelling x-axis
plt.ylabel('Y-axis')                #Labelling y-axis
plt.title('Learning Matplotlib')    #Adding Title
plt.show()
'''

#Adding a Legend
x = np.arange(5)
plt.plot(x, x, label= 'Linear')
plt.plot(x, x*x, label= 'Square')
plt.plot(x, x*x*x, label= 'Cube')
plt.legend()
plt.axis([0,5,0,20])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Learning Matplotlib')
plt.savefig('myplot.png')
plt.show()