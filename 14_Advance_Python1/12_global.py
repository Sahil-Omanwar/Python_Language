#global keyword is used to change global variable

a=89
def fun():
    global a
    a=3
    print(a)

fun()
print(a)