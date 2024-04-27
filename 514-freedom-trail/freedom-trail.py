class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        R, K = len(ring), len(key)
        @cache
        def solve(r, k):
            if k == K: return 0

            ch = key[k]

            if ring[r] == ch: return solve(r, k + 1) + 1

            pos1, cnt1 = r, 0
            while ring[pos1] != ch:
                pos1 = pos1 + 1 if pos1 < R - 1 else 0
                cnt1 += 1
            
            pos2, cnt2 = r, 0
            while ring[pos2] != ch:
                pos2 = pos2 - 1 if pos2 > 0 else R - 1
                cnt2 += 1
            
            return min(solve(pos1, k+1) + cnt1 + 1, solve(pos2, k + 1) + cnt2 + 1)
    
        return solve(0, 0)