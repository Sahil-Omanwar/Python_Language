#multiplication table using for in reverse

n=int(input("Enter n : "))

for i in range(n,0,-1):
    print(f"{n}*{i}={n*i}")