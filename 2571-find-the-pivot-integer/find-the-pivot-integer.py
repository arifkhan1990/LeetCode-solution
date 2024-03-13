class Solution:
    def pivotInteger(self, n: int) -> int:
        sm = n*(n+1) // 2
        m = int(sqrt(sm))
        if m*m == sm:
            return m
        return -1