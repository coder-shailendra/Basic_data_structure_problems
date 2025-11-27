import math

n = float(input("Enter a non-negative number: "))
if n < 0:
    print("Square root of negative number is not a real number.")
else:
    root = math.sqrt(n)
    print("Square root:", root)
