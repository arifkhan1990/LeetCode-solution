class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        d = res = 0
        for i in range(len(gain)):
            d += gain[i]
            res = max(res,d)
        return res