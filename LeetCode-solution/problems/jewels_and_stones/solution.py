class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for i in jewels:
            if i in stones:
                ans += stones.count(i)
        return ans