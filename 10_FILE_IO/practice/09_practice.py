#program to know if two files are identical

with open("this.txt") as f:
    content=f.read()
with open("copy_this.txt")as g:
    content1=g.read()

if(content1==content):
    print("Yes both the files are identical")
else:
    print("No both files are not identical")

