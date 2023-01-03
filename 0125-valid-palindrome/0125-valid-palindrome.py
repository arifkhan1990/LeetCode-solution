import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        data = re.sub(r'[^0-9a-zA-Z]', '', s)
        return True if data.lower() == data[::-1].lower() else False
            