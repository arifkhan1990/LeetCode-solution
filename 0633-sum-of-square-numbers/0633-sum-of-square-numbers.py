import math
class Solution:
    
    def judgeSquareSum(self, c: int) -> bool:
        # i = 0
        # while i*i <= c:   # TLE
        #     b = c - i*i
        #     j , sm = 1, 0
        #     while sm < b:
        #         sm += j
        #         j += 2
        #     if sm == b:
        #         return 1
        #     i += 1
        # return 0
        
        i = 0
        while i*i <= c: 
            b = math.sqrt(c - i*i)
            if b == int(b):
                return 1
            i += 1
        return 0