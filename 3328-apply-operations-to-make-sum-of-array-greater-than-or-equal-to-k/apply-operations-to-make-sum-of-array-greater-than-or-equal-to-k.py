class Solution:
    def minOperations(self, k: int) -> int:
        ans = float('inf')
        for i in range(k+1):
            ans = min(ans, i + (k-1) // (i+1))
        return ans