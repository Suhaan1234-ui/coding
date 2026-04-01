import matplotlib.pyplot as plt
import numpy as np
#matplotlib is a library in python used for data visualization. It provides a wide range of functions and tools to create various types of plots and charts, such as line plots, scatter plots, bar plots, histograms, and more. The pyplot module is a part of the matplotlib library that provides a simple interface for creating and customizing plots. By importing pyplot as plt, we can use its functions to create and manipulate our visualizations.
x=np.array([1,2,3,4,5])
y=np.array([2,3,5,7,11]) #much faster
plt.plot(x,y) # this will create a line plot of the data points defined by the x and y lists. The plot function takes the x and y values as arguments and creates a line plot connecting the points defined by those values. In this case, it will create a line plot with the x values [1, 2, 3, 4, 5] and the corresponding y values [2, 3, 5, 7, 11].
plt.show()

#plt.plot(y) this will create a line plot with the x interval of 0.5 and point marking at 1,2,3 etc