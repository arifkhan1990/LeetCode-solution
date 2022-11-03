class Solution:
    def countPoints(self, rings: str) -> int:
        d = {}
        i = 0
        while i < len(rings):
            if rings[i+1] in d:
                d[rings[i+1]].append(rings[i])
            else:
                d[rings[i+1]] = [rings[i]]
            i += 2
        ans = 0
        for i in d:
            if len(set(d[i])) == 3:
                ans += 1
        return ans