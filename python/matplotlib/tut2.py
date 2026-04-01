#plot customization
import matplotlib.pyplot as plt
import numpy as np
linestyle = {
    "marker": "o",
    "markersize": 10,
    "markerfacecolor": "red",
    "markeredgecolor": "blue",
    "markeredgewidth": 2,
    "linestyle": "dashed",
    "linewidth": 2,
}
x=np.array([1,2,3,4,5])
y1=np.array([2,3,5,7,11])
y2=np.array([1,4,9,16,25])


plt.plot(x,y1,**linestyle,color="blue") # ** is used to unpack the dictionary and pass the key-value pairs as keyword arguments to the plot function. This allows us to specify the styling options for the plot using a dictionary, which can make our code cleaner and more organized. In this case, we are passing the linestyle dictionary to the plot function, which will apply the specified styling options to the line plot.
plt.plot(x,y2,**linestyle,color="green")
plt.show()