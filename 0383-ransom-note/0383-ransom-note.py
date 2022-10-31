class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r = collections.Counter(ransomNote)
        m = collections.Counter(magazine)
        for i in r:
            if i not in m or r[i] > m[i]:
                return 0
        return 1