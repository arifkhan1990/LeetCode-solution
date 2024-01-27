class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []


        def solve(i, subset):
            if len(subset) == k:
                ans.append(subset.copy())
                return
            for j in range(i, n+1):
                subset.append(j)
                solve(j+1, subset)
                subset.pop()
        solve(1, [])
        return ans