#make a copy of  text file this.txt in copy_this


with open("this.txt") as f:
    content=f.read()
    g=open("copy_this.txt","w")
    g.write(content)

    g.close()
