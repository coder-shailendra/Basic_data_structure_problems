def Add_Digits(num):
    while num >= 10:         
        sum_digits = 0
        while num > 0:        
            sum_digits += num % 10
            num //= 10
        
        num = sum_digits      
    
    return num

#Example
print(Add_Digits(38))  
print(Add_Digits(45))