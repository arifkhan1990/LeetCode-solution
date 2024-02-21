class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        notMatch = 0
        while left != right:
            left >>= 1
            right >>= 1
            notMatch += 1
        left <<= notMatch
        return left