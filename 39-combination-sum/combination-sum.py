class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        sunsets = []
        def solve(s,t,p):
            if t == 0:
                ans.append(p[:])
                return
            
            for i in range(s, len(candidates)):
                if candidates[i] > t:
                    continue
                p.append(candidates[i])

                solve(i, t-candidates[i], p)
                p.pop()

        candidates.sort()
        solve(0, target, [])

        return ans
