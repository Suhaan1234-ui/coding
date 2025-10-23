a=open("file.txt")
print(a.read())
a.close()
#in this we have to manually open and clsoe a file , we can do the same without opening and closing
# manually using with   
with open("file.txt") as a:
      print(a.read())