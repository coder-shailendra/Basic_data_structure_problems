def second_largest(arr):
    if len(arr) < 2:
        return "Array should have at least 2 elements"

    first = second = float('-inf')

    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num

    if second == float('-inf'):
        return "No second largest element"
    
    return second
print(second_largest([10, 20, 4, 45, 99]))
print(second_largest([5, 5, 5]))