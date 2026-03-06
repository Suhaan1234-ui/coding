n=int(input("enter a number"))
for i in range(1,n+1):
   if(i==1 or i==n):
       print("*"*n,end="")
   else :
       print("*" + " "*(n-2) +"*", end="")
   print()
       #In the previous code we did not use end="" in the print statement, which means that after printing each line of stars, it would automatically move to the next line. This is the default behavior of the print function in Python.
       #However, in this code, we are using end="" in the print statement, which means that after printing each line of stars, it will not move to the next line and will instead continue printing on the same line. This allows us to create a hollow square pattern of stars, where the first and last lines are filled with stars, and the lines in between have stars only at the beginning and end, with spaces in between.
       