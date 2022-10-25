class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        c = Counter(nums).values()
        ans = exN = 0
        for i in c:
            ans += i//2
            exN += i%2
        return [ans, exN]