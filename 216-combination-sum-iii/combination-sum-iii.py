class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def solve(s, t, p):

            if t == 0 and len(p) == k:
                ans.append(p[:])
                return

            for i in range(s, 10):
                p.append(i)
                solve(i+1, t-i, p)
                p.pop()

        solve(1, n, [])
        return ans