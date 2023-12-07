class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0

        for char in s:
            if char.isalpha():
                size += 1
            else:
                size *= int(char)

        for char in reversed(s):
            k %= size
            if k == 0 and char.isalpha():
                return char
            if char.isalpha():
                size -= 1
            else:
                size //= int(char)
        return ""