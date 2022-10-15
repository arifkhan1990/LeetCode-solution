#User function Template for python3

class Solution:
    def digitSumCheck(self,n):
        digitSum = 0
        while n!=0:
            digitSum += n%10
            n //= 10
        return 1 if digitSum%2 == 0 else 0
        
    def stringGenerate(self,n,flick):
        s = 'abcdefghijklmnopqrstuvwxyz'
        return s[:n] if flick == 0 else s[-n:]
        
    def BalancedString(self,N):
        s = 'abcdefghijklmnopqrstuvwxyz'
        ans = s*(N//26)
        N = N - len(ans)

        if N%2:
            if self.digitSumCheck(len(ans)+N):
                ans += s[:(N+1)//2] + s[26 - (N-1)//2:]
            else:
                ans += s[:((N-1)//2)] + s[26 - (N+1)//2:]
        else:
            ans += s[:N//2] + s[26 - N//2:]
            
        return ans
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        
        ob=Solution()
        print(ob.BalancedString(N))
# } Driver Code Ends