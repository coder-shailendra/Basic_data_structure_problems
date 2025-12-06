def isUgly(n):
    if n <= 0:
        return False
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    return n == 1
num = int(input("Enter a number: "))

if isUgly(num):
    print(num, "is an Ugly Number")
else:
    print(num, "is NOT an Ugly Number")
