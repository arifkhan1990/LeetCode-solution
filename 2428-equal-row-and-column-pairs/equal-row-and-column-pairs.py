class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        convert = defaultdict(int)

        for row in grid:
            convert[tuple(row)] += 1
        
        for col in zip(*grid):
            ans += convert[tuple(col)]
        return ans
        # this is another solution

        # matrix = grid.copy()
        # transposed_matrix = []
        # for i in range(len(matrix[0])):
        #     transposed_row = []
        #     for row in matrix:
        #         transposed_row.append(row[i])
        #     transposed_matrix.append(transposed_row)
        
        # ans = 0
        # for i in range(len(matrix[0])):
        #     for j in range(len(matrix[0])):
        #         if grid[i] == transposed_matrix[j]:
        #             ans += 1
        # return ans