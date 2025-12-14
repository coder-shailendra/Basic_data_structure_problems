def isPowerOfTwo(n):
    return n > 0 and (n & (n - 1)) == 0


# Example
print(isPowerOfTwo(32)) 
print(isPowerOfTwo(45))  