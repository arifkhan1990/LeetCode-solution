def solve(nb, ne):
    ans = nb
    em = nb

    while em >= ne :
        ans += 1
        em -= ne
        em += 1
        ne += 1
    return ans

nb = 20
ne = 1
print(solve(nb, ne))