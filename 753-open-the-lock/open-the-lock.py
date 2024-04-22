class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        
        q = deque([('0000', 0)])
        visited = set(['0000'])

        while q:
            curr, step = q.popleft()
            if curr == target:
                return step
            
            if curr in deadends:
                continue
            
            for i in range(4):
                for m in [-1, 1]:
                    new_state = curr[:i] + str((int(curr[i]) + m)%10) + curr[i+1:]

                    if new_state not in visited and new_state not in deadends:
                        q.append((new_state, step+1))
                        visited.add(new_state)
        return -1