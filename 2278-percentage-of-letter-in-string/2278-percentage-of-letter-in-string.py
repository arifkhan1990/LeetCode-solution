class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        c = s.count(letter)
        a = 100/len(s)
        return floor(a*c)