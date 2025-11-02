def find_average(numbers):
    total=sum(numbers)
    avg=total / len(numbers)
    return(avg)
v=[5,10,15,20,25,30,35,40]
print("average is:",find_average(v))