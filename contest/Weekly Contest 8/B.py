# TLE 
# def solve(arr, idx, sum1, sum2):
#     if idx == len(arr):
#         return sum1 == sum2
    
#     if solve(arr, idx + 1, sum1 + arr[idx], sum2):
#         return 1
#     if solve(arr, idx + 1, sum1,  sum2 + arr[idx]):
#         return 1
    
#     return 0

def solve(nums):
    total_sum = sum(nums)
        
    if total_sum%2:
        return 0
    
    target_sum = total_sum // 2
    dp = [0] * (target_sum + 1)
    dp[0] = 1
    
    for n in nums:
        for i in range(target_sum, n - 1, -1):
            dp[i] = dp[i] or dp[i-n]
            
    return dp[target_sum]
# Example usage:
arr = [1,5,11,5]
print(solve(arr))