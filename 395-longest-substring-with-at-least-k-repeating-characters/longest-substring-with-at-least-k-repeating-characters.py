class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if k == 0:
            return len(s)

        st = {}
        mxL = -1
        for i in range(len(s)):
            if s[i] in st:
                st[s[i]] += 1
            else:
                st[s[i]] = 1

        for c in st:
            if st[c] < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(c))

        return len(s)