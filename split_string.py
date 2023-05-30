def split_string(string):
    alphabetic_chars = []
    numeric_chars = []
    special_symbols = []

    for char in string:
        if char.isalpha():
            alphabetic_chars.append(char)
        elif char.isdigit():
            numeric_chars.append(char)
        else:
            special_symbols.append(char)

    return alphabetic_chars, numeric_chars, special_symbols


input_string = "aBc&123D!10"
alphabetic, numeric, special = split_string(input_string)

print("Alphabetic characters:", ''.join(alphabetic))
print("Numeric characters:", ''.join(numeric))
print("Special symbols:", ''.join(special))
