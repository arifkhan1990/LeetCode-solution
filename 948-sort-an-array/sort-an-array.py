class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            
            mid = len(nums)//2
            l_half, r_half = nums[:mid], nums[mid:]
            l, r = merge_sort(l_half), merge_sort(r_half)
            return merge(l, r)
        
        def merge(l, r):
            arr = []
            l_idx, r_idx = 0, 0

            while l_idx < len(l) and r_idx < len(r):
                if l[l_idx] < r[r_idx]:
                    arr.append(l[l_idx])
                    l_idx += 1
                else:
                    arr.append(r[r_idx])
                    r_idx += 1
            arr.extend(l[l_idx:])
            arr.extend(r[r_idx:])

            return arr
        return merge_sort(nums)