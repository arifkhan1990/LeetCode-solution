class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row_sum = [0] * n
        col_sum = [0] * m
        ans = 0

        # Calculate row_sum and col_sum arrays
        for i in range(n):
            for j in range(m):
                row_sum[i] += mat[i][j]
                col_sum[j] += mat[i][j]

        # Check for special elements
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 1 and row_sum[i] == 1 and col_sum[j] == 1:
                    ans += 1

        return ans