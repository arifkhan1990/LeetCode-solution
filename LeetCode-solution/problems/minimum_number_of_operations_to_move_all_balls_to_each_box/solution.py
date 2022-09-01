class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        
        for i, r in enumerate(boxes):
            for j in range(i):
                if r == '1':
                    ans[j] += abs(i-j)
            for j in range(i+1, len(boxes)):
                if r == '1':
                    ans[j] += abs(i-j)
        return ans