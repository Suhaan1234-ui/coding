badwords=["donkey","gande","bekar","chinar"]
with open("p46source.txt") as a:
    read=a.read()
for a in badwords:
    read=read.replace(a,"#"*len(a))
with open("p46source.txt","w") as f:
    f.write(read)