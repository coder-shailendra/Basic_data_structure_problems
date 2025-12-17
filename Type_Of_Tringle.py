def type_of_triangle(num):
    a , b , c  = num
    if a + b <= c or b + c <=a or c + a <= b:
        return "none"
    elif a==b==c:
        return "equilateral"
    elif a==b or b==c or c==a:
        return "isoscenes"
    else:
        return "scalene"
print(type_of_triangle([3,3,4]))
print(type_of_triangle([1,2,3]))
print(type_of_triangle([3,3,3]))
print(type_of_triangle([4,5,6]))
