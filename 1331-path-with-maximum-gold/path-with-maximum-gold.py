class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x,y,curr_gold):
            nonlocal mx_gold

            orginal_gold = grid[x][y]
            grid[x][y] = 0
            curr_gold += orginal_gold
            mx_gold = max(mx_gold, curr_gold)

            for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                nx,ny = x + dx, y+dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] > 0:
                    dfs(nx,ny, curr_gold)
            grid[x][y] = orginal_gold

        mx_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        return mx_gold