class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        cnt = 0
        rm = 0
        fre = {0: 1}

        for i in nums:
            rm += i
            dif = rm - goal
            if dif in fre:
                cnt += fre[dif]
            fre[rm] = fre.get(rm, 0) + 1
        return cnt