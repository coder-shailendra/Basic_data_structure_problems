def int_to_roman(num):
    
    roman_values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman_symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    
    
    for i in range(len(roman_values)):
        while num >= roman_values[i]:
            result += roman_symbols[i]  
            num -= roman_values[i]      
    
    return result

# Example
number = 2645
print("Roman numeral:", int_to_roman(number))
