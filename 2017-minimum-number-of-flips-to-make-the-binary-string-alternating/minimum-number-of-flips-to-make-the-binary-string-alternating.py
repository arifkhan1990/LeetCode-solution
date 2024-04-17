class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s
        s1, s2 = "", ""

        for i in range(len(s)):
            s1 += '0' if i%2 else '1'
            s2 += '1' if i%2 else '0'
        
        ans = float('inf')
        cnt1,cnt2 = 0, 0
        l = 0
        for r in range(len(s)):
            if s[r] != s1[r]:
                cnt1 += 1
            if s[r] != s2[r]:
                cnt2 += 1
            
            if r - l + 1 > n:
                if s[l] != s1[l]:
                    cnt1 -= 1
                if s[l] != s2[l]:
                    cnt2 -= 1
                l += 1
            
            if r - l + 1 == n:
                ans = min(ans, cnt1, cnt2)
        return ans