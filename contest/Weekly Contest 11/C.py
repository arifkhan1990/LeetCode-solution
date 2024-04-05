from collections import Counter


def count_unique_substrings(s):
    i, x = 0, Counter()
    while i < len(s):
        x[ord(s[i])] = max(x[ord(s[i])], 1)
        j = i + 1
        while j < len(s) and (ord(s[j]) - ord(s[j-1]) == 1 or ord(s[j]) - ord(s[j-1]) == -25):
            j += 1
            x[ord(s[j - 1])] = max(x[ord(s[j-1])],  j - i)
        i = j
    return sum(x.values())

# Test the function
# print(count_unique_substrings("a"))   # Output: 1
# print(count_unique_substrings("cac")) # Output: 2
print(count_unique_substrings("zab")) # Output: 6
