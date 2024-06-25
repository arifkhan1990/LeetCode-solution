class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        rev_num = int(num[::-1])
        return str(rev_num)[::-1]