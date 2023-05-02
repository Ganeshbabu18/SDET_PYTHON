def longest_common_substring(str_one: str, str_two: str) -> int:
    len_one, len_two = len(str_one), len(str_two)
    table = [[0] * (len_one + 1) for _ in range(len_two + 1)]
    max_len = 0
    for i in range(1, len_one + 1):
        for j in range(1, len_two + 1):
            if str_one[i - 1] == str_two[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                max_len = max(max_len, table[i][j])
    return max_len


str_one = "abcdxyz"
str_two = "xyzabcd"
print(longest_common_substring(str_one, str_two))
