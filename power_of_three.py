def isPowerOfthree(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n = n // 3

    return n == 1
print(isPowerOfthree(9))  
print(isPowerOfthree(81)) 
print(isPowerOfthree(15))  