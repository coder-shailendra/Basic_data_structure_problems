def maximumproduct(numbers):
    numbers.sort()
    product1 = numbers[-1]*numbers[-2]*numbers[-3]
    product2 = numbers[0]*numbers[1]*numbers[-1]
    return max(product1,product2)
print(maximumproduct([1,2,3,]))
print(maximumproduct([-3,-2,-1]))