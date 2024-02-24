class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = defaultdict(list)
        for m in meetings:
            x, y, t = m
            g[x].append([y, t])
            g[y].append([x, t])
        
        v = [0]*n
        s = [(0, 0), (0, firstPerson)]
        heapq.heapify(s)
        
        while s:
            t, x = heapq.heappop(s)
            if v[x]:
                continue
            v[x] = 1
            for it in g[x]:
                if v[it[0]]:
                    continue
                if it[1] >= t:
                    heapq.heappush(s, (it[1], it[0]))
        ans = []
        for i in range(n):
            if v[i]:
                ans.append(i)
        return ans