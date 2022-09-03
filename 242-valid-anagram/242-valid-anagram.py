class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = collections.Counter(s)
        m = collections.Counter(t)
        
        if len(s) != len(t):
            return False
        for c in s:
            if c not in m or m[c] < r[c]:
                return False
        
        return True