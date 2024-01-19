import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(((point[0]*point[0]) + (point[1]*point[1])), [point[0], point[1]]) for point in points]
        heapq.heapify(heap)

        ans = []

        for _ in range(k):
            fre, point = heapq.heappop(heap)
            ans.append(point)
        
        return ans