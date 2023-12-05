class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        for i in range(len(words)):
            words[i] = sorted(words[i])
        
        ans = 0
        dupli = []
        for i in words:
            if i not in dupli:
                a = words.count(i)
                ans += a//2
                dupli.append(i)
            
        return ans
        

        