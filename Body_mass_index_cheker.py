weight=float(input("enter the weight of the people "))
if weight<18.5:
    print("under weight")
elif weight>18.5 and weight<24.9:
    print("normal")
elif weight>24.9 and weight<29.9:
    print("over weight")
else:
    print("obese")