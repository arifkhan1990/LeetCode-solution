class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range((n+1)//2):
            if(n%2):
                if(i == n//2):
                    ans.append(0)
                else:
                    ans.append((n-i)*-1)
                    ans.append(n-i)
            else:
                ans.append((n-i)*-1)
                ans.append(n-i)
        return ans