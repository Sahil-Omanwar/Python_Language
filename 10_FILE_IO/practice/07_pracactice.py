#line number where python is present in 6

#for lop with eles
with open("log.html") as f:
    lines=f.readlines()
    lineno = 1
    for line in lines:

       if("python" in line):
        print(f"Yes python is present in line :{lineno}")
        break
        lineno+=1
    else:
        print("No python is not present in line")

