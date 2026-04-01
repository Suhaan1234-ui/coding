#filtering in keeping only the rows that satisfy a certain condition
import pandas as pd
data=pd.read_csv("data.csv",index_col="Name")
waterpok=data[(data["Type1"]=="Water") & (data["Type2"]=="Psychic")] 