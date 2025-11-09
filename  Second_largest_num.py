def second_largest(lst):
    lst = list(set(lst))  
    lst.sort()
    return lst[-2]

nums = [53,95,80,55,65,43,76,54,66,65,43]
print("Second Largest:", second_largest(nums))