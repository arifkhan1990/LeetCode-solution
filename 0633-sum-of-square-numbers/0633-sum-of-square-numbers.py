import math
class Solution:
    # def binarySearch(self, l, h , t):
    #     if l > e:
    #         return 0
    #     m = l + (h - l)//2
    #     # print(m , m*m, t)
    #     if (m*m) == t:
    #         return 1
    #     if (m*m) > t:
    #         return self.binarySearch(l, m-1, t)
    #     return self.binarySearch(m+1, h , t)
    
    def judgeSquareSum(self, c: int) -> bool:
        # Fermat Theorem
        i = 2
        while i*i <= c:
            co = 0
            if c%i == 0:
                while c%i == 0:
                    co += 1
                    c /= i
                if i%4 == 3 and co % 2 != 0:
                    return 0
            i += 1
        return c%4 != 3
            
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
        
        # sqrt approch
        # i = 0
        # while i*i <= c: 
        #     b = math.sqrt(c - i*i)
        #     if b == int(b):
        #         return 1
        #     i += 1
        # return 0
       # binary search and sqrt
        # i = 0
        # while i*i <= c:
        #     b = c - (i*i)
        #     if self.binarySearch(0,b , b):
        #         return 1
        #     i += 1
        # return 0
        