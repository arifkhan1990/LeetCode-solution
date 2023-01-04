from collections import Counter
class Solution:  
    def minimumRounds(self, tasks: List[int]) -> int:
        task = sorted(tasks)
        round = Counter(task)
        ans = 0
        for x in round.keys():
            if round[x] >= 2 and round[x]%3 == 0:
                ans += round[x]//3
            elif round[x] >= 2 and round[x]%3 == 1:
                ans += (round[x]//3)-1 + 2
            elif round[x] >= 2 and round[x]%3 == 2:
                ans += (round[x]//3) + 1
            else:
                ans = -1
                break
        return ans