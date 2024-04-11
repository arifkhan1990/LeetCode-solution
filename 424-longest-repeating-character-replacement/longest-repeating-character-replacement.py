class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, n, ans = 0, 0, len(s), 0
        mxch = 0
        x = [0]*26
        for r in range(n):
            x[ord(s[r]) - ord('A')] += 1
            mxch = max(mxch, x[ord(s[r]) - ord('A')])
            if  (r - l + 1) - mxch <= k:
                ans = max(ans, r - l + 1)
            else:
                x[ord(s[l]) - ord('A')] -= 1
                l += 1
        return ans

