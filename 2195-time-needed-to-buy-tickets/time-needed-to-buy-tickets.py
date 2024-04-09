class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        mx = tickets[k]
        for i, n in enumerate (tickets):
            if n >= mx:
                ans += mx
            else:
                ans += n

            if i > k and n >= mx:
                ans -= 1


        return ans