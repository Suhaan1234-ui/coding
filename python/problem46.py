with open("p46source.txt") as a:
    text=a.read()
newtext=text.replace("donkey","######")
with open ("p46source.txt","w") as f:
    f.write(newtext)