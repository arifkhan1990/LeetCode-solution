class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []

        def solve(idx, subset):
            if idx == len(s):
                ans.append("".join(subset))
                return
            
            ch = s[idx]
            if ch.isalpha():
                solve(idx+1, subset+[ch.lower()])
                solve(idx+1, subset+[ch.upper()])
            else:
                solve(idx+1, subset+[ch])
        solve(0, [])
        return ans
