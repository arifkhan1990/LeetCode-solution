class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashT = {}
        dupli = []
        
        for i , c in enumerate(s):
            if (c not in dupli) and (c not in hashT):
                hashT[c] = i
            else:
                if c not in dupli:
                    hashT.pop(c)
                dupli.append(c)

        return -1 if len(hashT) == 0 else list(hashT.values())[0]