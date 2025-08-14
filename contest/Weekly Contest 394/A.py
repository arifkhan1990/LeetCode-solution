def count_special_letters(word):
    ans = 0
    for i in set(word):
        if i >= 'a' and i <= 'z':
            if i.upper() in word:
                ans += 1
    return ans

# Example usage:
word1 = "aaAbcBC"
word2 = "abcXx"

print(count_special_letters(word1))  # Output: 3
print(count_special_letters(word2))  # Output: 0

