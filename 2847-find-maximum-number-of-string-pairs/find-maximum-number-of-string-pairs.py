class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        word_set = set(words)
        result = 0

        for word in words:
            rev_word = word[::-1]
            if rev_word in word_set and word != rev_word:
                result += 1
                word_set.remove(word)
                word_set.remove(rev_word)

        return result
        

        