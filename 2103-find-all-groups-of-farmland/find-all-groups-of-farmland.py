class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols =  len(land), len(land[0])
        visited = set()
        ans = []

        def bfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            mn_r,mn_c, mx_r, mx_c = r,c,r,c
            while q:
                row, col = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r, c = dr+row, dc+col
                    if (r in range(rows) and
                        c in range(cols) and
                        land[r][c] == 1 and
                        (r,c) not in visited):
                        visited.add((r,c))
                        q.append((r,c))
                        mn_r = min(mn_r, r)
                        mn_c = min(mn_c, c)
                        mx_r = max(mx_r, r)
                        mx_c = max(mx_c, c)
            return [mn_r, mn_c, mx_r, mx_c]

        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 and (r,c) not in visited:
                    ans.append(bfs(r,c))
        return ans

