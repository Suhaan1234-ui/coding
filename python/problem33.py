# n=int(input("enter any number"))
# for i in range (1,n+1):
#     for k in range (n-i):
#         print(" ")
#     for j in range (2*i-1):
#         print("*")
# print("\n")#range function automatically handles the newline after each print statement so the 
#cpp logic wont work here
#to not get default newline in python use end="" in print statement
n=int(input("enter any number"))
for i in range (1,n+1):
    for k in range (n-i):
        print(" ",end="")
    for j in range (2*i-1):
        print("*",end="")
    print(  )

    #or we can also make it simpler
n=int(input("enter any number")) 
for a in range(1,n+1):
    print(" "*(n-a)+ "*"*(2*a-1))