class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sL = list(s.split())
        newS = ' '.join(sL[:k])
        return newS