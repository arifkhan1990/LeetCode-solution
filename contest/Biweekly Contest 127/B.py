def minimumLevels(possible):
    total = 0
    for v in possible:
        if v == 0:
            total -= 1
        else:
            total += 1
    n = len(possible)
    cur = 0
    for i in range(n-1):
        if possible[i] == 0:
            cur -= 1
        else:
            cur += 1
        if total - cur < cur:
            return i+1
    return -1

# Test case
print(minimumLevels([1, 0, 1, 0]))  # Output: 1
