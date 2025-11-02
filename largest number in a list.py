def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
nums = [10, 25, 7, 90, 56]
print("Largest number is:", find_largest(nums))
