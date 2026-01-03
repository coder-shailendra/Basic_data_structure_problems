num=(input("enter the number :"))
result = ""
for i in range(len(num) - 1, -1, -1):
    if int(num[i]) % 2 == 1:
        result = num[:i + 1]
        break
print(result)