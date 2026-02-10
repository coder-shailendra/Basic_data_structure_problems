def isPerfectSquare(num):
    i = 1
    while i * i <= num:
        if i * i == num:
            return True
        i += 1
    return False
print(isPerfectSquare(16))
print(isPerfectSquare(20))
