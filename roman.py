def roman_to_decimal(roman_numeral):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(roman_numeral):
        current_value = roman_dict[char]
        
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        prev_value = current_value
    
    return total
roman_numeral = input("Enter a Roman Numeral: ").upper()
decimal_num = roman_to_decimal(roman_numeral)
print(f"The Decimal Equivalent of {roman_numeral} is {decimal_num}.")
