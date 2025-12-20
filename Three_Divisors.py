def Three_divisors(n):
    if n < 4:
        return False

    root = int(n ** 0.5)

    if root * root != n:
        return False
    for i in range(2, int(root ** 0.5) + 1):
        if root % i == 0:
            return False
    return True
print(Three_divisors(4))
print(Three_divisors(6))
print(Three_divisors(45))
print(Three_divisors(9))