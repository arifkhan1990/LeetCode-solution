class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len1, len2 = len(s), len(t)
        if len1 < len2:
            return ""
        else:
            hash_t = [0] * 256 
            hash_s = [0] * 256 
    
            for i in range(len2): 
                hash_t[ord(t[i])] += 1 
    
            start = 0
            start_index = -1
            min_len = float("inf")
            count = 0
    
            for j in range(len1): 
    
                hash_s[ord(s[j])] += 1
    
                if (hash_t[ord(s[j])] != 0 and hash_s[ord(s[j])] <= hash_t[ord(s[j])] ):
                    count += 1 
    
                if (count == len2): 
    
                    while ( hash_s[ord(s[start])] > hash_t[ord(s[start])] or hash_t[ord(s[start])] == 0): 
    
                        if (hash_s[ord(s[start])] > hash_t[ord(s[start])]): 
                            hash_s[ord(s[start])] -= 1 
    
                        start += 1 
    
                    len_window = j - start + 1; 
    
                    if (min_len > len_window): 
    
                        min_len = len_window 
                        start_index = start 
    
            if (start_index == -1):
                return ""
    
            else:
                return s[start_index:min_len+start_index]