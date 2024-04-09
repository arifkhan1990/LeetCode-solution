class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        n = len(people)-1
        i = 0
        w, ans = 0, 0
        people.sort()
        while i <= n:
            if people[i]+people[n] > limit:
                ans += 1
                n -= 1
            else:
                ans += 1
                i += 1
                n -= 1
        return ans