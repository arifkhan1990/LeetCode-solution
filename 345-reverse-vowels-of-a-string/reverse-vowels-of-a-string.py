class Solution:
    def reverseVowels(self, s: str) -> str:
        i , j = 0, len(s)-1
        s = list(s)
        while i < len(s) and  j >= 0 and i < j:
            if s[i] in 'aeiouAEIOU' and s[j] in 'aeiouAEIOU':
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] not in 'aeiouAEIOU' and s[j] not in 'aeiouAEIOU':
                i += 1
                j -= 1
            elif s[i] not in 'aeiouAEIOU':
                i += 1
            elif s[j] not in 'aeiouAEIOU':
                j -= 1

        return "".join(s)

