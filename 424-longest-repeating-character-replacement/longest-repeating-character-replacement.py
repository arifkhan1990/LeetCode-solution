class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mxl , mxc, l = 0, 0, 0

        char_cnt = [0]*26

        for r in range(len(s)):
            char_cnt[ord(s[r]) - ord('A')] += 1
            mxc = max(mxc, char_cnt[ord(s[r])-ord('A')])

            if (r - l + 1) - mxc > k:
                char_cnt[ord(s[l]) - ord('A')] -= 1
                l += 1
            mxl = max(mxl, r - l + 1)
        return mxl