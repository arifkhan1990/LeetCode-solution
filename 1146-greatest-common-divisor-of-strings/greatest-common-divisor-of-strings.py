class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def strGcd(a, b):
            if b == 0:
                return a
            return strGcd(b, a%b)
            
        gcd_len = strGcd(len(str1), len(str2))
        gcd_substr = str1[:gcd_len]
        
        return gcd_substr if str1 + str2 == str2 + str1 else ""
        