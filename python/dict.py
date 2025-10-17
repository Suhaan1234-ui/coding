dict1={"marks":78,
       "list1":[1,2,3],
         "dict2":{"name":"rohan","age":20},
         6:True
       }
print(dict1)
print(type(dict1))
print(dict1[6])#accessing value using key
print(dict1["dict2"]["name"])#accessing nested dictionary value



print(dict1.items())
print(dict1.keys())
print(dict1.values())
dict1.update({"marks": 99, "Renuka": 100})
print(dict1)

print(dict1.get("marks")) 
print(dict1["marks"])
print(dict1.get("marks2")) # Prints None
#print(dict1["marks2"]) # Returns an error