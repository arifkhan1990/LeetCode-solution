class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        tree = collections.defaultdict(list)
        for p, c in edges:
            tree[p].append(c)
            tree[c].append(p)
        
        def dfs(cur, p):
            totalTime = 0
            for c in tree[cur]:
                if c == p:
                    continue
                currTime = dfs(c, cur)
                if currTime or hasApple[c]:
                    totalTime += 2 + currTime
            return totalTime
        return dfs(0, -1)