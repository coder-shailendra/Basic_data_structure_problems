def isPerfectNumber(num):
    total = 0   
    for i in range(1, num):
        if num % i == 0:    
            total = total + i
    if total == num:
        return True
    else:
        return False
print(isPerfectNumber(7))
print(isPerfectNumber(28))
print(isPerfectNumber(45))
print(isPerfectNumber(12))