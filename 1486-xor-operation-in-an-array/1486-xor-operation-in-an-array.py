class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i = 0
        k = 0
        while i < n:
            k ^= start + 2*i
            i += 1
        return k
            