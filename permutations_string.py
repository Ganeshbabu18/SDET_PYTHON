import itertools

string = "abb"
perms = itertools.permutations(string)

for perm in perms:
    print(''.join(perm))