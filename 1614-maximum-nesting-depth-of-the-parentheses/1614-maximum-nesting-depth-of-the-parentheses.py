class Solution:
    def maxDepth(self, s: str) -> int:
        ans = 0
        p = []
        for i in s:
            if i == '(':
                p.append(i)
            if len(p) != 0 and i == ')':
                ans = max(ans,len(p))
                p.pop()
        return ans