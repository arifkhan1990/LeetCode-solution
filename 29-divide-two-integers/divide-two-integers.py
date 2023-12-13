class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle special cases
        if dividend == 0:
            return 0
        if divisor == 1:
            return min(max(dividend, INT_MIN), INT_MAX)
        if divisor == -1:
            return min(max(-dividend, INT_MIN), INT_MAX)

        # Determine sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        # Convert both dividend and divisor to positive
        dividend, divisor = abs(dividend), abs(divisor)

        quotient = 0
        while dividend >= divisor:
            current_divisor, multiple = divisor, 1
            while dividend >= current_divisor:
                dividend -= current_divisor
                quotient += multiple

                current_divisor <<= 1  # Left shift to double the divisor
                multiple <<= 1  # Left shift to double the multiple

        result = sign * quotient

        # Handle overflow cases
        return min(max(result, INT_MIN), INT_MAX)
