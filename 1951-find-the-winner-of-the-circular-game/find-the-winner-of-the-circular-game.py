from collections import deque
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n+1))
        
        while len(q) > 1:
            remove = k - 1
            for _ in range(remove):
                q.append(q.popleft())
            q.popleft()
        return q[0]