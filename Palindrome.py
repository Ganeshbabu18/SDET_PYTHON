# python program for palindrome or not without slicing method
def is_palindrome(s):
    s = s.lower().replace(" ", "")

    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - i - 1]:
            return False
    return True


s = input("Enter a string: ")
if is_palindrome(s):
    print(s, "is a palindrome.")
else:
    print(s, "is not a palindrome.")
