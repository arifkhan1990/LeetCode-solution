class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_freq = {}
        for char in words[0]:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        for word in words[1:]:
            temp_freq = {}
            for char in word:
                temp_freq[char] = temp_freq.get(char, 0) + 1
            for char in char_freq.keys():
                char_freq[char] = min(char_freq[char], temp_freq.get(char, 0))
        
        result = []
        for char, freq in char_freq.items():
            result.extend([char] * freq)
        
        return result