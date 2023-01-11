class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s1 = {}
        t1 = {}
        for k,v in zip(s, t):
            if k not in s1 and v not in t1:
                s1[k], t1[v] = v, k
            elif s1.get(k) != v or t1.get(v) != k:
                return False
        return True