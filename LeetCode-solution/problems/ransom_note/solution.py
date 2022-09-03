class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        
        for c in ransomNote:
            if c not in m or r[c] > m[c]:
                return False
        
        return True