write= "i love watching anime \n"* 5
a=open("file2.txt","w")   #opening file in write mode and createing a new file if not exists
a.write(write)
a.close()


# a=open("file2.txt","w").write("i love watching anime")
#closing is not necessary here as file is closed automatically after writing