class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        k = 0
        i, j = 1, 0
        while i <= n:
            for k in range(1,8):
                if i > n:
                    break
                ans += k+j
                
                if i%7 == 0:
                    j += 1

                i += 1

        return ans

        