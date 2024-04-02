class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        smp = {}
        tmp = {}

        for i in range(len(s)):
            if s[i] not in smp and t[i] not in tmp:
                smp[s[i]] = t[i]
                tmp[t[i]] = s[i]
            elif  (s[i] not in smp and t[i] in tmp) or  (s[i] in smp and t[i] not in tmp):
                return 0
            else:
                if smp[s[i]] != t[i] or tmp[t[i]] != s[i]:
                    return 0
        return 1

