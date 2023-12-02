class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = float('inf')
        nums.sort()
        for i in range(n-2):
            j = i + 1
            k = n - 1
            while j < k:
                a = (nums[i]+nums[j]+nums[k])
                if a == target:
                    return a
                if abs(a- target) < abs(ans - target):
                    ans = a
                
                if a - target > 0:
                    k -= 1
                else:
                    j += 1
        return ans
