class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = list(s.split())[::-1]
        return " ".join(list_s)
        