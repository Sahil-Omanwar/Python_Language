#rename the name of initial.txt to renamed.txt

with open("initial.txt")as f:
    content=f.read()

with open("renamed.txt")as f:
    f.write(content)