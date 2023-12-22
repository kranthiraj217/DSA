def first_non_repeating_char(input_str):
    char_count = {}
    
    # Count occurrences of each character in the string
    for char in input_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    # Find the first character with count 1 (non-repeated)
    for char in input_str:
        if char_count[char] == 1:
            return char
    
    # If no non-repeated character found
    return None

# Example usage:
input_string = "abacdefbce"
result = first_non_repeating_char(input_string)

if result:
    print(f"The first non-repeated character is: {result}")
else:
    print("No non-repeated character found.")
