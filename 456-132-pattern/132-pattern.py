class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        mn = nums[0]
        st = []
        for i in nums:
            while st and i >= st[-1][0]:
                st.pop()
            
            if st and i > st[-1][1]:
                return 1
            
            st.append([i, mn])
            mn = min(mn, i)
        return 0
        