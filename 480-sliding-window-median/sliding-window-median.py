class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(ar, k):
            if k%2 == 0:
                return float((ar[k//2] + (ar[k//2  - 1]))/2)
            else:
                return float(ar[k//2])

        x = sorted(nums[:k])
        ans = [median(x, k)]
        for i in range(k, len(nums)):
            x.remove(nums[i-k])

            newEle_pos = bisect.bisect_left(x, nums[i])
            x.insert(newEle_pos, nums[i])

            ans.append(median(x, k))

        return ans
