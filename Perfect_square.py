def is_perfect_square(num):
    root = int(num ** 0.5)
    return root * root == num

print(is_perfect_square(2))  
print(is_perfect_square(625))  