from array import array

def sum_array(arr):
    total = 0
    for i in arr:
        total += i
    return total
nums = array('i', [1, 2, 3, 4])
print(sum_array(nums))  
