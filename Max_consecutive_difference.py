arr={2,3,5,7,8,5,32,22,1,12,32,22}
max_diff = max(abs(arr[i] - arr[i-1]) for i in range(1, len(arr)))
print(max_diff)