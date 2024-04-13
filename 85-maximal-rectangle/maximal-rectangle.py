class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def largestRectangleArea(heights):
            stack = []
            maxArea = 0
            heights.append(0)  # Append a zero height to handle the last element
            
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    maxArea = max(maxArea, h * w)
                stack.append(i)
            
            heights.pop()  # Remove the appended zero height
            return maxArea
            
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        maxArea = 0
        height = [0] * cols
        
        for i in range(rows):
            # Update the height array based on the current row
            for j in range(cols):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            # Calculate the maximum rectangle area using the current height array
            maxArea = max(maxArea, largestRectangleArea(height))
        
        return maxArea

