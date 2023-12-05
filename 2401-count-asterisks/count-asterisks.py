class Solution:
    def countAsterisks(self, s: str) -> int:
        in_pair = False
        star_count = 0

        for char in s:
            if char == '|':
                in_pair = not in_pair
            elif char == '*' and not in_pair:
                star_count += 1

        return star_count