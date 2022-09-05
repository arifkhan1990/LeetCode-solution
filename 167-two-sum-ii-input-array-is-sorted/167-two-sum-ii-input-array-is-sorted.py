class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo , hi = 0, len(numbers)-1
        
        while lo <= hi:
            if numbers[lo] + numbers[hi] > target:
                hi = hi - 1
            elif numbers[lo] + numbers[hi] < target:
                lo = lo+1
            else:
                return [lo+1, hi+1]
        return []