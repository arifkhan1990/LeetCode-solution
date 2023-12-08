class Solution:
    def isNumber(self, s: str) -> bool:
        # Define the regular expression pattern for a valid number
        pattern = re.compile(r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$')
        
        # Check if the string matches the pattern
        return bool(pattern.match(s.strip()))