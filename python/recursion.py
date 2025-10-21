def fact(n):
    if(a==0 or a==1): #base condition to stop recursion
        return 1
    return n*fact(n-1)
a=int(input("enter a number"))
print(fact(a))      