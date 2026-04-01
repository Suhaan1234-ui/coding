#aggregate function = reduces a set of values into a single summarize values, 
#used to summarizem and analyze data , often used with the groupby() function
import pandas as pd
data =pd.read_csv("data.csv")
#for whole dataframe
print(data.mean(numeric_only=True))
print(data.max(numeric_only=True))
print(data.sum(numeric_only=True))
print(data.min(numeric_only=True))
print(data.count())#counts values in each column
print(data["Height"].mean())