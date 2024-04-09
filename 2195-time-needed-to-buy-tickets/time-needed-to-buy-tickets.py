class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        mx = tickets[k]
        for i, n in enumerate (tickets):
            if i <= k:
                if n >= mx:
                    ans += mx
                else:
                    ans += n
            else:
                if n >= mx:
                    ans += mx-1
                else:
                    ans += n

        return ans