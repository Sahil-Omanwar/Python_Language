#to know if log file contains python

with open("log.html","r") as f:
    content=f.read()

if('python' in content):
    print("Yes python is present in log file ")
else:
    print("No python is not present in the file ")