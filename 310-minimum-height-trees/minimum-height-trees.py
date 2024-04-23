class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_list = defaultdict(set)
        for edge in edges:
            u, v = edge
            adj_list[u].add(v)
            adj_list[v].add(u)
        
        leaves= [node for node in adj_list if len(adj_list[node]) == 1]

        while n > 2:
            new_leaves = []
            n -= len(leaves)
            for leaf in leaves:
                neighbor = adj_list[leaf].pop()
                adj_list[neighbor].remove(leaf)
                if len(adj_list[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves