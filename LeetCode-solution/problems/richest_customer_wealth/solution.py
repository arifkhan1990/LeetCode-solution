class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ansAmount = 0
        for i in accounts:
            currentAccSum = sum(i)
            ansAmount = max(ansAmount, currentAccSum)
        return ansAmount