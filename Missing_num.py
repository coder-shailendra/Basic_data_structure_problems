def find_missing_number(nums):
    n = len(nums) + 1                 
    total_sum = n * (n + 1) // 2      
    array_sum = sum(nums)
    return total_sum - array_sum
print(find_missing_number([1,2,4,5,6]))