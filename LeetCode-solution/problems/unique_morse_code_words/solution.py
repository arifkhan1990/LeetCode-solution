class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        letterDic = {}
        morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        englishLetter = 'abcdefghijklmnopqrstuvwxyz'
        for count, char in enumerate(englishLetter):
            letterDic[char] = morseCode[count]
            
        ans = []
        
        for w in words:
            morseW = ''
            for c in w:
                morseW += letterDic[c]
            if morseW not in ans:
                ans.append(morseW)
        return len(ans)