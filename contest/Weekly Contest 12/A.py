def dis_closest(house, heaters):
    l, r = 0, len(heaters)-1
    dis = float("inf")
    while l <= r:
        m = (l+r)//2
        dis = min(dis, abs(heaters[m] - house))
        if heaters[m] < house:
            l = m + 1
        else:
            r = m - 1
    return dis

def solve(houses, heaters):
    heaters.sort()
    ans = 0
    for i in houses:
        ans = max(ans, dis_closest(i, heaters))
    return ans

houses = [1,2,3,4]
heaters = [1,4]
print(solve(houses, heaters))