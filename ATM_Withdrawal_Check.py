amount = int(input("Enter withdrawal amount: "))

if amount % 100 == 0:
    print("Withdrawal Successful!")
else:
    print("Error: Amount must be a multiple of 100.")

