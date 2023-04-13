# Python program to count repeated characters in a string and display the count of repeated characters

String = "GANESH BABU"
char_count = {}

for char in String:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

for char, count in char_count.items():
    if count > 1:
        print(f"Character '{char}' occurs '{count}' times.")