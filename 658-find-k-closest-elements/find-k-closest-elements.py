class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - 1

        # Use sliding window approach
        while right - left + 1 > k:
            left_diff = abs(arr[left] - x)
            right_diff = abs(arr[right] - x)

            # Remove the element with a larger absolute difference
            if left_diff > right_diff:
                left += 1
            else:
                right -= 1

        # Return the k closest elements
        return arr[left:right + 1]