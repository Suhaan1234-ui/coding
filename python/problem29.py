list=[]
n=int(input("enter the number of names"))
for i in range(n):
    name=input("enter the name")
    list.append(name)
i = 0
while(i<n):
    print(f"good afternoon {list[i]}")
    i=i+1