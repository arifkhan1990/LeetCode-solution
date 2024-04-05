def solve(turnedOn):
    ans = []
    for h in range(12):
        for m in range(60):
            if (bin(h) + bin(m)).count('1') == turnedOn:
                t = '%d:%02d'% (h, m)
                ans.append(t)
    return ans

print(solve(1))