n=int(input("enter a number"))
for i in range (1,n+1):
    print("*"*i) #in this line we are multiplying the string "*" with the value of i, which will print the string "*" i times.
    # So for example, when i is 1, it will print "*", when i is 2, it will print "**", and so on. This creates a pattern of stars that increases in number with each line.
    #we are not using end="" here because we want to print each line of stars on a new line, which is the default behavior of the print function in Python.