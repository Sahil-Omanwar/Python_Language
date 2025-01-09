try:
    a=int(input("Enter a number : "))
    print(a)

except Exception as e:
    print(e)


##We can also specify the exception to catch
try:
    b=int(input("Enter a number : "))
    print(b)

except ValueError as v:
    print(v)
except Exception as e:
    print(e)