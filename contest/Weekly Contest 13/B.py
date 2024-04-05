def solve(x, y):
    xor_ans = bin((x^y))[2:]
    return xor_ans.count('1')

nums = [4,14,4]
ans = 0
for i in range(32):
    bits = sum((num >> i) & 1 for num in nums)
    cnt_bit = len(nums) - bits
    ans += bits * cnt_bit
print(ans)
