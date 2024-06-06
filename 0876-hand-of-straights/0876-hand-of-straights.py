class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1
        
        hand.sort()  # Sort the hand
        
        for card in hand:
            if counts[card] > 0:
                for i in range(groupSize):
                    if card + i not in counts or counts[card + i] < 1:
                        return False
                    counts[card + i] -= 1
        return True