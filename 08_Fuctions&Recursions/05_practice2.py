#celcius to fahrenheit
#f=(c*(9/5))+32


c=int(input("Enter the temperature in celcius"))

def cel_fah(c):
    f = (c * (9 / 5)) + 32
    return f

ans=cel_fah(c)
print(f"{c} to fahrenhrith is: {ans}")