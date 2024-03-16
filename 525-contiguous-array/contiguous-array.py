class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        mxl, cnt = 0, 0
        m = {0:-1}

        for i in range(len(nums)):
            if nums[i] == 0:
                cnt -= 1
            else:
                cnt += 1
            
            if cnt in m:
                mxl = max(mxl, i - m[cnt])
            else:
                m[cnt] = i
        return mxl