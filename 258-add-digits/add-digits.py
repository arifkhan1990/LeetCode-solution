class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            sm = num
            x = 0
            while sm != 0:
                x += sm%10
                sm //= 10
            num = x
        return num