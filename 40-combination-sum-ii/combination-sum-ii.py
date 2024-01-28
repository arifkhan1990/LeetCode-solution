class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(s, t, p):
            if t == 0:
                ans.append(p[:])
                return
            
            for i in range(s, len(candidates)):
                if i > s and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > t:
                    continue

                p.append(candidates[i])
                solve(i+1, t-candidates[i], p)
                p.pop()
        candidates.sort()
        solve(0, target, [])
        return ans