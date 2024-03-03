class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        t = len(graph) - 1
        ans = []

        def dfs(node, p):
            if node == t:
                ans.append(p[:])
                return
            
            for n in graph[node]:
                dfs(n, p + [n])
        dfs(0, [0])
        return ans