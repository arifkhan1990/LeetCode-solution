def permutation_difference(s, t):
    # Create dictionaries to store indices of characters in s and t
    indices_s = {}
    indices_t = {}
    
    # Iterate over each character in s and store its index
    for i, char in enumerate(s):
        indices_s[char] = i
    
    # Iterate over each character in t and store its index
    for i, char in enumerate(t):
        indices_t[char] = i
    
    # Calculate permutation difference
    difference = 0
    for char in s:
        difference += abs(indices_s[char] - indices_t[char])
    
    return difference

# Example usage:
s = "abc"
t = "bca"
print(permutation_difference(s, t))  # Output: 4
