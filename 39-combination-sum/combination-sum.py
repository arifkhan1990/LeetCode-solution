class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(s, t,p):
            if t == 0:
                ans.append(p[:])
                return
            
            for i in range(s, len(candidates)):
                if candidates[i] > t:
                    continue
                p.append(candidates[i])

                backtrack(i, t-candidates[i], p)
                p.pop()
        ans = []
        candidates.sort()
        backtrack(0, target, [])
        return ans