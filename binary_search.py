data = [2, 4, 6, 8, 10]
key = 7
low = 0
high = len(data) - 1
found = False
while low <= high:
    mid = (low + high) // 2
    if data[mid] == key:
        found = True
        break
    elif key < data[mid]:
        high = mid - 1
    else:
        low = mid + 1
if found:
    print("Found")
else:
    print("Not Found")
