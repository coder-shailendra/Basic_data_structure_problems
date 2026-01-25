"""name = input("Enter your name: ")
print("Welcome", name)"""

'''ame = "Amit"
age = 20
print(f"My name is {name} and age is {age}")'''


"""for i in range(1, 10):
    if i == 5:
        break
    print(i)"""

"""for i in range(1, 6):
    if i == 3:
        continue
    print(i)"""

"""lst = [1, 2]
lst.append(3)
print(lst)

lst = [5, 1, 4]
lst.sort()
print(lst)


a = [1, 2]
b = a.copy()
print(b)

t = (1, 2, 2, 3)
print(t.count(2))
print(t.index(3))

t = (10, 20, 30)
print(20 in t)"""

"""my_set = {1, 2, 3, 3}
print(my_set)


s1 = {10, 20, 30}
s2 = {"Python", "Java"}
s3 = {1, "Hello", 3.5}

A = {1, 2}
B = {2, 3}
print(A | B)
print(A & B)
print(A - B)
print(A ^ B)



s = {1, 2, 3}
s.add(4)
print(s)"""


"""s = {1, 2}
s.update([3, 4, 5])
print(s)


s = {1, 2, 3}
s.discard(3)
print(s)

s = {10, 20, 30}
s.pop()
print(s)


def add(a, b):
    print(a + b)

add(10, 5)

lst = [10, 20, 30, 40, 50]
key = 30

for i in lst:
    if i == key:
        print("Element found")
        break


numbers = [5, 10, 15, 20]
key = 25

found = False
for i in numbers:
    if i == key:
        found = True

if found:
    print("Element Found")
else:
    print("Element Not Found")


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
    print("Not Found")"""
