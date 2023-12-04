class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        stack = []
        seen = set()

        # Count occurrences of each character
        for item in s:
            if item not in counter:
                counter[item] = 1
            else:
                counter[item] += 1

        for char in s:
            counter[char] -= 1

            if char in seen:
                continue

            # Pop characters from the stack if they are greater and there are more occurrences later
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            seen.add(char)
            stack.append(char)

        return ''.join(stack)