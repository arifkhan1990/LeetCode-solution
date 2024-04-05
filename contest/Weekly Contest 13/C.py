def can_form_square(nums):
        if not nums:
            return  0
        
        total = sum(nums)
        
        if total % 4 != 0:
            return 0
        
        nums.sort(reverse=True)
        
        def backtrack(idx, sides):
            if idx == len(nums):
                return all(side == 0 for side in sides)
            
            for i in range(4):
                if sides[i] >= nums[idx]:
                    sides[i] -= nums[idx]
                    if backtrack(idx + 1, sides):
                        return 1
                    sides[i] += nums[idx]
            return 0
        return backtrack(0, [total // 4] * 4)
# Example usage:
nums = [1, 1, 2, 2, 2]
print(can_form_square(nums))  # Output: True