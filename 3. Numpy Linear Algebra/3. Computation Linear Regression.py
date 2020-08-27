# Numpy Mathematical Calculations
# Linear Regression

# numpy.linalg.lstsq() method

import numpy as np
import matplotlib.pyplot as plt
import random
# x co-ordinates
x = np.arange(0,20, 0.5)

print("x=",x)
l= len(x)
A = np.array([x, np.ones(l)])

print("A=",A)



y = []

for i in range(0, l):
    # any random numbers from 0 to 20
    y.append(random.randint(0, 20))
    
print("y=",y)

# obtaining the parameters of regression line
w = np.linalg.lstsq(A.T, y)[0] 

# plotting the line
line = w[0]*x + w[1] # regression line
plt.plot(x, line, 'r-')
plt.plot(x, y, 'o')
plt.show()


