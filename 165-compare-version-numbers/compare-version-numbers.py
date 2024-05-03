class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a, b = version1.split('.'), version2.split('.')
        n1 = len(a)
        n2 = len(b)
        i = 0
        
        # Compare each corresponding part
        while i < n1 or i < n2:
            # Get the integer value of the current part or default to 0 if not present
            num1 = int(a[i]) if i < n1 else 0
            num2 = int(b[i]) if i < n2 else 0
            
            # Compare the parts
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
            
            # Move to the next part
            i += 1
        if n1 < n2:
            # Check if remaining parts in version2 are all zeros
            for j in range(n1, n2):
                if int(b[j]) > 0:
                    return -1
            return 0
        elif n1 > n2:
            # Check if remaining parts in version1 are all zeros
            for j in range(n2, n1):
                if int(a[j]) > 0:
                    return 1
            return 0
        else:
            return 0
