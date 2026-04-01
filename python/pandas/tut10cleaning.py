#data cleaning = the process of identifying and correcting or removing errors, inconsistencies, and inaccuracies in a dataset to improve its quality and reliability for analysis. It involves tasks such as handling missing values, removing duplicates, correcting data types, and standardizing formats. Data cleaning is an essential step in the data analysis process as it ensures that the data is accurate, consistent, and ready for analysis.75 percent of pandass users use it for data cleaning
import pandas as pd
data = pd.read_csv("data.csv") 
#removing irrelevent colums
#data=data.drop(columns=["Type2"]) # this will remove the column "Type2" from the DataFrame "data". The drop function is used to remove specified labels from rows or columns. In this case, we are using it to remove the column "Type2" by specifying it in the columns parameter. The resulting DataFrame will no longer contain the "Type2" column.

#removing specific rows
data=data.drop(index=[0,1]) # this will remove the rows at index 0 and index 1 from the DataFrame "data". The drop function is used to remove specified labels from rows or columns. In this case, we are using it to remove the rows at index 0 and index 1 by specifying them in the index parameter. The resulting DataFrame will no longer contain the rows at index 0 and index 1.

#handling missing values
data=data.dropna(subset=["Type2"]) # this will remove the rows from the DataFrame "data" where the value in the "Type2" column is missing (NaN). The dropna function is used to remove missing values from a DataFrame. In this case, we are using it to remove rows that have missing values in the "Type2" column by specifying it in the subset parameter. The resulting DataFrame will only contain rows where the "Type2" column has non-missing values.

#filling missing values
data["Type2"]=data["Type2"].fillna("None") # this will fill the missing values in the "Type2" column of the DataFrame "data" with the string "None". The fillna function is used to fill missing values in a DataFrame. In this case, we are using it to replace any missing values in the "Type2" column with the string "None". The resulting DataFrame will have all missing values in the "Type2" column replaced with "None".
#na mean replace the not available with somethingelse 

#fixing incosistent data
data["Type1"]=data["Type1"].replace("Fire","fire") # this will replace all occurrences of the string "Fire" with the string "fire" in the "Type1" column of the DataFrame "data". The replace function is used to replace specified values in a DataFrame. In this case, we are using it to replace any occurrences of "Fire" with "fire" in the "Type1" column. The resulting DataFrame will have all instances of "Fire" in the "Type1" column replaced with "fire".

#standardizing formats
data["Name"]=data["Name"].str.lower() # this will convert all characters in the "Name"column to lowercase

#fix data types
data["Legendary"]=data["Legendary"].astype(bool) # this will convert the data type of the "Legendary" column in the DataFrame "data" to boolean (True/False). The astype function is used to cast a pandas object to a specified data type. In this case, we are using it to convert the values in the "Legendary" column to boolean values, where any non-zero or non-empty value will be considered True and any zero or empty value will be considered False. The resulting DataFrame will have the "Legendary" column with boolean data type.

#fixing duplicates
#data=data.drop_duplicates() # this will remove duplicate rows from the DataFrame "data". The drop_duplicates function is used to remove duplicate rows from a DataFrame. By default, it considers all columns to identify duplicates, but you can also specify specific columns to consider for identifying duplicates. The resulting DataFrame will only contain unique rows, with any duplicate rows removed.