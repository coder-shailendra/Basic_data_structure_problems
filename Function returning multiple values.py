def calc(a, b):
    return a + b, a - b, a * b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
add, sub, mul = calc(a, b)
print("Addition:", add)
print("Subtraction:", sub)
print("Multiplication:", mul)