a=()
b=[]
print(type(a))
print(type(b))  
#tuples are immutable whereas lists are mutable
# b[0]=100
# print(b)#b is an empyt list so 0 index is not present gives error
b.append(100)
print(b)