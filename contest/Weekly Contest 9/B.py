
import collections
# e = 0,1,3(2),5,7(2),8,9
# g = 8
# f = 4,5
# i = 5,6,8,9
# h = 3,8
# o = 0,1,2,4
# n = 1,7,9(2)
# s = 6,7
# r = 0,3,4
# u = 4
# t = 3,8
# w = 2
# v = 5,7
# x = 6
# z = 0

s = "owoztneoer"
dp = [0]*10

cnt =collections.Counter(s)
dp[0] = cnt['z']
dp[2] = cnt['w']
dp[4] = cnt['u']
dp[8] = cnt['g']
dp[6] = cnt['x']

dp[1] = cnt['o'] - dp[0] - dp[2] - dp[4]
dp[3] = cnt['h'] - dp[8]
dp[5] = cnt['f'] - dp[4]
dp[7] = cnt['s'] - dp[6]
dp[9] = cnt['i'] - dp[5] - dp[6] - dp[8]

ans = ""
for i in range(10):
    while dp[i] > 0:
        ans += str(i)
        dp[i] -= 1
print(ans)


