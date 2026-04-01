import matplotlib.pyplot as plt
import numpy as np
#piechart 
categories=["math","science","english","history"]
values=[25, 30, 15, 30]
plt.pie(values,labels=categories,autopct="%1.1f%%",shadow=True,
        explode=[0.1,0,0,0],startangle=45) 
# this will create a pie chart with the specified values and labels. The pie function takes the values and labels as arguments and creates a pie chart based on those values. The autopct argument is used to display the percentage of each category on the pie chart, with the format specified as "%1.1f%%" (which means one decimal place followed by a percentage sign). The startangle argument is used to specify the starting angle of the pie chart, which in this case is set to 90 degrees. The shadow argument is set to True to add a shadow effect to the pie chart. The explode argument is used to specify how much each slice of the pie should be "exploded" or separated from the center, with the first slice (math) being exploded by 0.1 and the others remaining at their default position.
plt.title("Subject Distribution",fontsize=20,family="serif",color="purple")
plt.show()