a=open("p43source.py")
reading=a.read()
if("twinkle" in reading):
    print("the keyword is present")
else:
    print("the keyword is not present")   #return statement can only be used inside a fucntion
a.close()

#or
with open("p43source.py") as a:
        reading=a.read()
        if("twinkle" in reading):
             print("present")
        else :
            print("not present")