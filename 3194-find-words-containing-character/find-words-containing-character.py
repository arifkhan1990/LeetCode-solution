from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return list(filter(lambda i: x in words[i], range(len(words))))

