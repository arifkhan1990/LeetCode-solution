class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        r = collections.Counter(s)
        m = collections.Counter(t)
        for i in 'abcdefghijklmnopqrstuvwsyz':
            if i in r and i in m:
                if r[i] != m[i]:
                    return 0
            elif i in r and i not in m:
                return 0
            elif i in m and i not in r:
                return 0
            
        return 1