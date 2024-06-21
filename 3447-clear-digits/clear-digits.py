class Solution:
    def clearDigits(self, s: str) -> str:
        s_list = list(s)
            # Function to find the closest non-digit character to the left of the given index
        def find_left_non_digit(index):
            for i in range(index - 1, -1, -1):
                if not s_list[i].isdigit():
                    return i
            return None

        while any(char.isdigit() for char in s_list):
            # Find the first digit
            first_digit_index = next(i for i, char in enumerate(s_list) if char.isdigit())
            
            # Find the closest non-digit character to the left of this digit
            left_non_digit_index = find_left_non_digit(first_digit_index)
            
            if left_non_digit_index is not None:
                # Remove both characters
                s_list[left_non_digit_index] = ''
                s_list[first_digit_index] = ''
            else:
                # If no non-digit character is found to the left, just remove the digit
                s_list[first_digit_index] = ''

            # Clean up any empty characters
            s_list = [char for char in s_list if char != '']

        # Join the list back to a string and return
        return ''.join(s_list)