age=int(input("enter the age "))
if age<0:
    print("invalid age")
elif age<=12:
    print("you are a Child")
elif age<=19:
    print("you are a Teenager")
elif age<=59:
    print("you are a Adult")
else:
    print("you are a Senior")