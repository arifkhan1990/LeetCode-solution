class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        v_cnt, l ,r, ans = 0, 0 ,0, 0

        for i in range(len(s)):
            if s[i] in "aeiou":
                v_cnt += 1
            if i - l + 1 > k:
                if s[l] in "aeiou":
                    v_cnt -= 1
                l += 1
            if i - l + 1 == k:
                ans = max(ans, v_cnt)
        return ans
            