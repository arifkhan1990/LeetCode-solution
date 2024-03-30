class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, slen, plen  = [], len(s), len(p)
        ph = [0]*26
        sh = [0]*26
        
        if slen < plen:
            return ans

        for i in range(plen):
            ph[ord(p[i]) - 97] += 1
            sh[ord(s[i]) - 97] += 1
        
        i, j  = plen-1, 0
        while i < slen:
            if sh == ph:
                ans.append(j)
            i += 1
            if i != slen:
                sh[ord(s[i]) - 97] += 1
            sh[ord(s[j]) - 97] -= 1
            j += 1
        return ans
