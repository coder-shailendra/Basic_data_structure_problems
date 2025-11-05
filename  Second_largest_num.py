def second_largest(lst):
    lst = list(set(lst))  
    lst.sort()
    return lst[-2]

nums = [12, 45, 23, 45, 67, 89]
print("Second Largest:", second_largest(nums))