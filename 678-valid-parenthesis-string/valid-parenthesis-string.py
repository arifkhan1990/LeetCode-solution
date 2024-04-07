class Solution:
    def checkValidString(self, s: str) -> bool:
        p = []
        p1 = 0
        p2 = 0
        star = 0
        for i in s:
            if i in "(":
                p1 += 1
                p2 += 1
            elif i == '*':
                p1 -= 1
                p2 += 1
            elif i == ')':
                p1 -= 1
                p2 -= 1
            
            if p2 < 0:
                return 0
            if p1 < 0:
                p1 = 0

        return p1 == 0