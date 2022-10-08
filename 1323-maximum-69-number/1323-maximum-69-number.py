class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        d = s.replace('6','9', 1)
        return d