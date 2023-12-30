class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch_set= set()
        mxl ,start = 0, 0

        for end in range(len(s)):
            while s[end] in ch_set:
                ch_set.remove(s[start])
                start += 1
            
            ch_set.add(s[end])
            mxl = max(mxl, end - start +1)
        return mxl
