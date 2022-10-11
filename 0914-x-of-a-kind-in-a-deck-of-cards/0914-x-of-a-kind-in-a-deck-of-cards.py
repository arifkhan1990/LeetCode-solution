import math
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        x = Counter(deck)
        y = 0
        if len(deck) == 1:
            return 0
        y = x[deck[0]]
        
        for i in x:
            y = math.gcd(y, x[i])
            if y == 1:
                return 0
        return 1