class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {'digit': 1, 'sign': 2, 'dot': 3},
            {'digit': 1, 'dot': 4, 'exp': 5},
            {'digit': 1, 'dot': 3},
            {'digit': 4},
            {'digit': 4, 'exp': 5},
            {'sign': 6, 'digit': 7},
            {'digit': 7},
            {'digit': 7}
        ]

        current_state = 0

        for char in s:
            if char.isdigit():
                key = 'digit'
            elif char == '.':
                key = 'dot'
            elif char in {'+', '-'}:
                key = 'sign'
            elif char in {'e', 'E'}:
                key = 'exp'
            else:
                return False

            if key not in states[current_state]:
                return False

            current_state = states[current_state][key]

        return current_state in {1, 4, 7}
