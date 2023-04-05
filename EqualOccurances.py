# Check if All Characters Have Equal Number of Occurrences
# Input: abacbc
from collections import Counter

def checkString(s):
    frequency = Counter(s)
    for i in frequency:
        if (frequency[i] % 2 == 1):
            return False
    return True

s = "abacbc"
if (checkString(s)):
    print("All Characters Have equal number of Occurrences")
else:
    print("All Characters have different number of Occurrences")