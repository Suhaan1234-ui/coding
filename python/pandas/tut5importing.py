import pandas as pd
data=pd.read_csv("data.csv") # this will read the data from the file "data.csv" and create a DataFrame object called "data". The read_csv function is used to read a comma-separated values (CSV) file into a DataFrame. The resulting DataFrame will have columns corresponding to the headers in the CSV file and rows corresponding to the data entries in the file.
print(data) # this will print the contents of the DataFrame "data" to the console
print(data.to_string()) # this will print the contents of the DataFrame "data" in a more readable format, with all the rows and columns displayed. The to_string function is used to convert the DataFrame into a string representation that can be printed to the console. By default, it will display all the rows and columns of the DataFrame, but you can also specify options to control how much of the DataFrame is displayed.
#similarly use excel file to read data from excel file we can use read_excel function
#data2=pd.read_excel("data.xlsx")   
