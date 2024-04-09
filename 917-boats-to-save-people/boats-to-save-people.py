class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)-1
        i, ans = 0, 0
        people.sort()
        while i <= n:
            if people[i]+people[n] <= limit:
                i += 1
            ans += 1
            n -= 1
        return ans