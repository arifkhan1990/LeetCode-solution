def count_substrings(s, c):
    n = len(s)
    count = 0
    count_of_c = 0
    for i in range(n):
        if s[i] == c:
            count_of_c += 1
        if s[i] == c:
            count += count_of_c
    return count

# Example usage:
s1 = "abada"
c1 = "a"
print(count_substrings(s1, c1))  # Output: 6

s2 = "zzz"
c2 = "z"
print(count_substrings(s2, c2))  # Output: 6

s3 = "ocu"
c3 = "o"
print(count_substrings(s3, c3))  # Output: 6
