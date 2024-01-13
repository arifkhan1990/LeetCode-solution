import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []
        
        ans = []
        heap = []
        
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i]+nums2[0], nums1[i],nums2[0], 0))

        while k > 0 and heap:
            _, u, v , index = heapq.heappop(heap)
            ans.append((u,v))

            if index+1 < len(nums2):
                heapq.heappush(heap, (u + nums2[index+1], u, nums2[index+1], index+1))

            k -= 1
        
        return ans