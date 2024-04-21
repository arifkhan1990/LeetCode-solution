class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q = deque()
        visited = set()
        visited.add(source)
        q.append(source)

        while q:
            node = q.popleft()
            if node == destination:
                return 1
            for n in graph[node]:
                if n not in visited:
                    visited.add(n)
                    q.append(n)
        return 0 
