list1=[1,"apple",3.5,True ,3.5, None]#lists are mutable
print(list1)
print(type(list1))#will show list as a class
print(list1[1])#indexing starts from 0
print(list1[0:3])#slicing
list1.pop(2)#removes element at index 2 and returns its value
print(list1)
print(list1.pop(2))
print(list1.pop())#removes last element and returns its value
#we can alsoe make nested lists
list2=[1,2,[3,4,5],6]
print(list2)
print(list2[2][1])#accessing nested list element    
list2[2][1]=100#modifying nested list element
print(list2)    