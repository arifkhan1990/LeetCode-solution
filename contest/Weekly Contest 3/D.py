def solve(s, k):
    if k == 0:
        return len(s)
    
    st = {}

    for i in range(len(s)):
        if s[i] in st:
            st[s[i]] += 1
        else:
            st[s[i]] = 1

    for c in st:
        if st[c] < k:
            return max(solve(sub_s, k) for sub_s in s.split(c))

    return len(s)

s = "ababbc"
k = 2
print(solve(s, k)) # Expected output: 3