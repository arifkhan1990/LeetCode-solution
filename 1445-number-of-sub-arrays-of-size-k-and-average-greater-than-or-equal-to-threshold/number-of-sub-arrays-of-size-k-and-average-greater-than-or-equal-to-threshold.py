class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        if len(arr) < k:
            return 0

        sm = sum(arr[:k-1])
        ans = 0
        j = 0
        for i in range(k-1,len(arr)):
            sm += arr[i]
            if sm//k >= threshold:
                ans += 1
            sm -= arr[j]
            j += 1
        return ans
            

