class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        result = [0] * len(deck)
        q = deque(range(len(deck)))
        
        for x in deck:
            i = q.popleft()
            result[i] = x
            
            if q:
                q.append(q.popleft())
        
        return result

