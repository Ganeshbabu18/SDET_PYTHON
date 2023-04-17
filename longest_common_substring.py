def longest_common_substring(X: str, Y: str) -> int:
    m, n = len(X), len(Y)
    table = [[0] * (n+1) for _ in range(m+1)]
    max_len = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                table[i][j] = table[i-1][j-1] + 1
                max_len = max(max_len, table[i][j])
    return max_len


X = "abcdxyz"
Y = "xyzabcd"
print(longest_common_substring(X, Y))