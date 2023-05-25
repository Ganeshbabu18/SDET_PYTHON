# Count The Number Of Vowels In A String
def count_vowels(string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_string = "Ganesh babu"

vowel_count = count_vowels(input_string)
print("Number of vowels:", vowel_count)