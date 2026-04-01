#labels
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
plt.xticks(x) # this will set the x-axis ticks to the values in the array x. The xticks function is used to specify the locations of the ticks{points} on the x-axis. By passing the array x as an argument, we are setting the ticks to be at the positions defined by the values in x, which are [1, 2, 3, 4, 5]. This will ensure that the x-axis ticks correspond to the data points we are plotting.
plt.tick_params(axis="both",color="purple",direction="inout",length=10,width=2) # this will customize the appearance of the ticks on both the x and y axes. The tick_params function is used to control the appearance of the ticks, including their color, direction, length, and width. In this case, we are setting the color of the ticks to purple, the direction to "inout" (which means the ticks will point both inward and outward), the length to 10, and the width to 2. This will make the ticks more visually distinct and easier to read on the plot.
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plot",fontsize=20,family="serif",color="purple",fontweight="bold")


plt.plot(x,y1,**linestyle,color="blue") # ** is used to unpack the dictionary and pass the key-value pairs as keyword arguments to the plot function. This allows us to specify the styling options for the plot using a dictionary, which can make our code cleaner and more organized. In this case, we are passing the linestyle dictionary to the plot function, which will apply the specified styling options to the line plot.
plt.plot(x,y2,**linestyle,color="green")
plt.show()