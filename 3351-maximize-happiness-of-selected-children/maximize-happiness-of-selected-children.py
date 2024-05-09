class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()  # Sort in non-ascending order
        total_happiness = 0
        j = 0
        ans = 0
        for i in range(len(happiness)-1, -1, -1):
            if k == j:
                break
            total_happiness += happiness[i] - j
            j += 1
            ans = max(ans, total_happiness)
        return ans