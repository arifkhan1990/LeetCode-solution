class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_seen_char = {}
        start = 0
        longest_string_len = 0
        
        for i, ch in enumerate(s):
            if ch in last_seen_char and last_seen_char[ch] >= start:
                start = last_seen_char[ch] + 1
            else:
                longest_string_len = max(longest_string_len, i - start + 1)
            
            last_seen_char[ch] = i
        
        return longest_string_len
        
        