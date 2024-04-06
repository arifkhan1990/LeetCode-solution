class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        num = list(set(nums))
        num.sort()
        
        ans = 1
        mx = 1
        for i in range(1, len(num)):
            if abs(num[i]-num[i-1]) == 1:
                ans += 1
            else:
                ans = 1
            mx = max(mx, ans)
        return mx