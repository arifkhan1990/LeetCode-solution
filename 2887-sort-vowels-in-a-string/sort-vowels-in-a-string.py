class Solution:
    def sortVowels(self, s: str) -> str:
        vowel = []
        for i in s:
            if i in "aeiouAEIOU":
                vowel.append(ord(i))
        vowel.sort()
        ans = ""
        vIdx = 0
        for i in s:
            if i in "aeiouAEIOU":
                ans += chr(vowel[vIdx])
                vIdx += 1
            else:
                ans += i
        return ans

        