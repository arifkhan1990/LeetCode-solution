import heapq
from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        min_cost = float('inf')

        q = [(0, src, 0)]
        visited = {}
        
        while q:
            cost, node, stops = heapq.heappop(q)
            
            if node == dst:
                min_cost = min(min_cost, cost)
                continue
            
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                if stops <= k:
                    for neighbor, weight in graph[node]:
                        heapq.heappush(q, (cost + weight, neighbor, stops + 1))
        
        return min_cost if min_cost != float('inf') else -1