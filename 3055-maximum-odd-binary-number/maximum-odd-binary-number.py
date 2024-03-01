class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        odd = s.count('1');
        l = len(s)
        ans = "1" * (odd - 1) + "0" * (l - odd) + "1"
        return ans
    