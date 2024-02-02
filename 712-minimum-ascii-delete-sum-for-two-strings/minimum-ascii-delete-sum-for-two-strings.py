class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}

        def solve(i, j, curr):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(s1) and j == len(s2):
                result = 0
            else:
                result = float('inf')

            if i < len(s1) and j < len(s2) and s1[i] == s2[j]:
                result = solve(i + 1, j + 1, curr)
            else:
                if i < len(s1):
                    result = min(result, ord(s1[i]) + solve(i + 1, j, curr))
                
                if j < len(s2):
                    result = min(result, ord(s2[j]) + solve(i, j + 1, curr))

            memo[(i, j)] = result
            return result

        return solve(0, 0, 0)