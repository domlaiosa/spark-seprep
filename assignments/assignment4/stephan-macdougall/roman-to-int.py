def roman_to_int(s: str) -> int:

    # Dictionary w/ values for Roman numerals
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0
    
    # Iterate over each character in the numeral left to right
    for char in s:
        # Get integer value of current Roman numeral
        curr_value = roman_values[char]
        
        # If the current value is greater than the previous value, it means
        # that a smaller numeral was before a larger one (subtraction case).
        if curr_value > prev_value:
            total += curr_value - 2 * prev_value  # Undo the previous addition and subtract instead
        else:
            total += curr_value
        
        # Update the previous value for the next iteration
        prev_value = curr_value
    
    return total
