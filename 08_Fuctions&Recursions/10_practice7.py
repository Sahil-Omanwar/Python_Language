#multiplication table

n=int(input("Enter the number : "))

def table(n):
    for i in range(1,11):
        print(f"{i}*{n}={i*n}")

table(n)
