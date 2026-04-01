#a dataframe is a tabular structure like a spreadsheet or a SQL table, where data is organized in rows and columns. It is a two-dimensional labeled data structure that can hold different types of data (e.g., integers, floats, strings) in each column. DataFrames are a fundamental data structure in the pandas library and are widely used for data manipulation and analysis in Python. They provide powerful tools for handling missing data, merging and joining datasets, and performing various operations on the data.
import pandas as pd
data = {""
"name":["Alice","Bob","Charlie","David"],
"age":[25,30,35,40],}
shop=pd.DataFrame(data,["store1","store2","store3","store4"]) 
print(shop)
print(shop.loc["store2"]) # this will print the row at index "store2" which contains the name "Bob" and age 30. The loc function is used to access a group of rows and columns by labels or a boolean array. In this case, we are using it to access a specific row based on its index label "store2".
print(shop.iloc[1]) # this will print the row at index 1, which is
shop["job"]=["engineer","doctor","teacher","artist"] # this will add a new column "job" to the DataFrame with the specified values for each row. The new column will contain the job titles corresponding to each person's name and age in the DataFrame.
print(shop)
newrow=pd.DataFrame([{"name":"Eve","age":28,"job":"lawyer"}, {"name":"Frank","age":35,"job":"chef"}],index=["store5", "store6"]) # this will create a new DataFrame with double row 
shop=pd.concat([shop,newrow]) # this will concatenate the original DataFrame "shop" with the new DataFrame "newrow", resulting in a new DataFrame that contains all the rows from both DataFrames. The concat function is used to concatenate pandas objects along a particular axis (in this case, we are concatenating along the rows, which is axis=0). The resulting DataFrame will have the same columns as the original DataFrame "shop" and will include the new rows from "newrow".
print(shop)
