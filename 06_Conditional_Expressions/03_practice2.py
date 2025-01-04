#determine if student pass or failed


total=int(input("Enter total marks : "))

math=int(input("Enter your math marks : "))
english=int(input("Enter your english marks : "))
science=int(input("Enter yout science marks : "))

math_per=(math*100)/total
english_per=(english*100)/total
science_per=(science*100)/total

total_per=(math+english+science)*100/(3*total)

if(total_per>40):
    if(math_per>=33 and english_per>=33 and science_per>=33):
        print("Passed sucessfully")
    else:
        print("Failed based on individual score")
else:
    print("Fail")