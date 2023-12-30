class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        mxl , l, zcnt = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zcnt += 1

            while zcnt > k:
                if nums[l] == 0:
                    zcnt -= 1
                l += 1

            mxl = max(mxl, r - l + 1)
        return mxl