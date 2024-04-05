class Solution:
    def firstUniqChar(self, s: str) -> int:
        data = {}
        for i, char in enumerate(s):
            if char in data:
                data[char] = -1  # Mark as not unique
            else:
                data[char] = i  # Store index of first occurrence
        # Find the first unique character's index
        for char, index in data.items():
            if index != -1:
                return index
        return -1