def max_happiness(happiness, k):
    happiness.sort()  # Sort in non-ascending order
    total_happiness = 0
    j = 0
    ans = 0
    for i in range(len(happiness)-1, -1, -1):
        if k == j:
            break
        total_happiness += happiness[i] - j
        j += 1
        ans = max(ans, total_happiness)
    return ans

# Test cases
print(max_happiness([1,2,3], 2))  # Output: 4
print(max_happiness([1,1,1,1], 2))  # Output: 1
print(max_happiness([2,3,4,5], 1))  # Output: 5
print(max_happiness([12,1,42], 3))  # Output: 5