class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        i = 0
        p = 0
        while(i<=num):
           j = int(str(i)[::-1])
           if(i+j == num):
               p = 1
               break
           i+=1 
        return 1 if p==1 else 0