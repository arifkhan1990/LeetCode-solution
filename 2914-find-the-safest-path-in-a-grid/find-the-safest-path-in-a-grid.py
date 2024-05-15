class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        distances = [[float('inf')] * n for _ in range(n)]
        queue = deque()
        
        # Initialize BFS from all thieves
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c))
                    distances[r][c] = 0
        
        # BFS to calculate minimum distance to any thief for each cell
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while queue:
            x, y = queue.popleft()
            current_dist = distances[x][y]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and distances[nx][ny] == float('inf'):
                    distances[nx][ny] = current_dist + 1
                    queue.append((nx, ny))
        
        # Function to check if a path with minimum safeness factor `k` exists
        def canReachWithSafeness(k):
            if distances[0][0] < k:
                return False
            visited = [[False] * n for _ in range(n)]
            queue = deque([(0, 0)])
            visited[0][0] = True
            while queue:
                x, y = queue.popleft()
                if x == n - 1 and y == n - 1:
                    return True
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and distances[nx][ny] >= k:
                        visited[nx][ny] = True
                        queue.append((nx, ny))
            return False
        
        # Binary search to find the maximum safeness factor
        low, high = 0, n + n - 2
        while low < high:
            mid = (low + high + 1) // 2
            if canReachWithSafeness(mid):
                low = mid
            else:
                high = mid - 1
        
        return low