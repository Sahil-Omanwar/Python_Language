try:
    b=int(input("Enter a number : "))
    print(b)


except Exception as e:
    print(e)

finally:
    print("Hey i am inside a finally")#finalyy always give output whether exception is their or not

#the main use of finally occurs in function where it run although return statement occurs above it
def main():
  try:
    b = int(input("Enter a number : "))
    print(b)
    return


  except Exception as e:
    print(e)
    return

  finally:
    print("Hey i am inside a finally")

main()
