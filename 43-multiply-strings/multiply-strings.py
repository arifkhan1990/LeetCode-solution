class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
    
        l1,l2 = len(num1), len(num2)
        ans = [0]*(l1+l2)

        for i in range(l1-1,-1,-1):
            for j in range(l2-1, -1,-1):
                mul = int(num1[i]) * int(num2[j])
                total = mul + (ans[i+j+1])
                ans[i+j+1] = total%10
                ans[i+j] += total//10
        return "".join(map(str,ans)).lstrip("0") or "0"