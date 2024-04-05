
def addStrings( num1: str, num2: str) -> str:
    carry = 0
    num1, num2 = num1[::-1], num2[::-1]
    n, m = len(num1), len(num2)
    ans = []
    for i in range(min(n, m)):
        digit1, digit2 = ord(num1[i]) - ord('0'),  ord(num2[i]) - ord('0')
        ans.append(chr(((digit1 + digit2 + carry) % 10) + ord('0')))
        carry = 1 if (digit1 + digit2 + carry) > 9 else 0

    for i in range(min(n,m), n):
        digit1 = ord(num1[i]) - ord('0')
        ans.append(chr(((digit1 + carry)%10) + ord('0')))
        carry = 1 if (digit1 + carry) > 9 else 0

    for i in range(min(n,m), m):
        digit2 = ord(num2[i]) - ord('0')
        ans.append(chr(((digit2 + carry)%10) + ord('0')))
        carry = 1 if (digit2 + carry) > 9 else 0
    
    if carry == 1:
        ans.append(chr(49))
    
    return "".join(ans[::-1])

print(addStrings("1","9"))