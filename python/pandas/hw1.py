import pandas as pd
data = pd.read_csv("data.csv",index_col="Name")
pokemon=input("Enter the name of the pokemon: ")
try:
    print(data.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found in the dataset.")  