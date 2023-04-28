def vowel_string(input_string):
    vowels = "AEIOUaeiou"
    result = ""

    for char in input_string:
        if char not in vowels:
            result += char.lower()

    result = " ".join(result)
    return result[::-1]


input_string = "Ganesh Babu"
reversed_string = vowel_string(input_string)

print("Result: ", reversed_string)
