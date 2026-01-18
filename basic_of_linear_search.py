numbers = [5, 10, 15, 20, 25, 30]
key = 15

found = False
for i in numbers:
    if i == key:
        found = True

if found:
    print("Element Found")
else:
    print("Element Not Found")
