def validIPAddress(IP: str) -> str:
    def isIPv4(s):
        try:
            return str(int(s)) == s and 0 <= int(s) <= 255
        except:
            return False

    def isIPv6(s):
        if len(s) > 4:
            return False
        try:
            return int(s, 16) >= 0 and s[0] != '-'
        except:
            return False

    if IP.count('.') == 3 and all(isIPv4(x) for x in IP.split('.')):
        return "IPv4"
    if IP.count(':') == 7 and all(isIPv6(x) for x in IP.split(':')):
        return "IPv6"
    return "Neither"

# Test cases
print(validIPAddress("192.168.1.1"))  # Output: IPv4
print(validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  # Output: IPv6
print(validIPAddress("256.256.256.256"))  # Output: Neither
print(validIPAddress("01.01.01.01"))  # Output: Neither