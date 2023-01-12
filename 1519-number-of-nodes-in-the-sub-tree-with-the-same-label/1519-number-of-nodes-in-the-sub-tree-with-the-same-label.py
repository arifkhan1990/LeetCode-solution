class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = collections.defaultdict(list)
        for p, c in edges:
            tree[p].append(c)
            tree[c].append(p)
        
        result = [None]*n
        
        def dfs(node, par):
            c_l = [0]*26
            
            for c in tree[node]:
                if c != par:
                    cnt = dfs(c, node)
                    for i in range(26):
                        c_l[i] += cnt[i]
            c_l[ord(labels[node]) - ord('a')] += 1
            result[node] = c_l[ord(labels[node]) - ord('a')]
            return c_l
        
        dfs(0, -1)
        return result