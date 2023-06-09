# Q: Python program to divide a string in 2 equal parts. Input string = "Ganeshbabu"

def divide_strings(string, n):
    length = len(string)
    if length % n != 0:
        print("Cannot divide the string into equal parts.")
        return []

    part_size = length // n
    parts = [string[i:i + part_size] for i in range(0, length, part_size)]
    return parts


# Input
strings_to_divide = "Ganeshbabu"
number_of_parts = 2

result = divide_strings(strings_to_divide, number_of_parts)
print(result)

# Output: ['Ganes', 'hbabu']
