class Solution:
    def minSwaps(self, s: str) -> int:
        ans, cur = 0, 0
        for i in s:
            if i == ']':
                cur += 1
            else:
                cur -= 1
            ans = max(ans, cur)
        return (ans+1)//2