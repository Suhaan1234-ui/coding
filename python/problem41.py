def strip(l,word):
    a=[]
    for i in l:
        if not(i==word):
            a.append(i.strip(word))
           
    return a
        