def ispronicnumber(num):
    for n in range (1,int(num**0.5)+1):
        if n*(n+1) == num:
            return True
    return False
print("pronic number between 1 to 100 are:")
for i in range (1,101):
    if ispronicnumber(i):
        print(i,end=" | ")    
print()