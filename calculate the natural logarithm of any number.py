import math
num = float(input("enter the number :"))
if num <= 0:
    print("please enter the positive number")
else:
    result = math.log(num)
    print(result)