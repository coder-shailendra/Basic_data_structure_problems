def all_unique(lst):
    return len(lst)==len(set(lst))

num=[1,2,3,5,9,8,7]
print(all_unique(num))

num=[1, 2, 3, 3, 4,4,7, 5]
print(all_unique(num))