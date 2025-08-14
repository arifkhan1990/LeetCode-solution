def solve(nums):
    cnt = 0
    ans = 0
    for i in nums:
        if i == 1:
            cnt += 1
        elif i != 1:
            ans = max(ans, cnt)
            cnt = 0
    ans = max(ans, cnt)
    return ans

nums = [1,1,0,1,1,1]
print(solve(nums))