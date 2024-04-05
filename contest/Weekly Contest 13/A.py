def solve(x, y):
    xor_ans = bin((x^y))[2:]
    return xor_ans.count('1')

x=1
y=4
print(solve(x, y))