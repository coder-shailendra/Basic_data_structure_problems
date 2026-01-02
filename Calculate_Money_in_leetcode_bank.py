n=int(input("enter the number:"))
week=0
day=0
total=0
for i in range(1,n+1):
    total += day+week+1
    day +=1
    if day==7:
        day=0
        week+=1
print(total)