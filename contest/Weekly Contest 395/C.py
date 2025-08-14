def findMinimumLastElement(n, x):
    n -= 1
    ans = x
    j = 0
    for i in range(30):
        while x >> j & 1:
            j += 1
        if n >> i & 1:
            ans |= 1 << j
        j += 1
    return ans

# Test cases
print(findMinimumLastElement(3, 4))  # Output: 6
print(findMinimumLastElement(2, 7))  # Output: 15

