#to rename a file we generally use os module to delte the original file then 
# make a copy of that file and rename it before deleting itin the followin way



with open("old.txt") as f:
    content = f.read()

with open("renamed_by_python.txt", "w") as f:
    f.write(content)

