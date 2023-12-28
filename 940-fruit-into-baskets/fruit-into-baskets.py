class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = {}
        tree = l = ans = 0

        for i in fruits:
            if i in cnt:
                cnt[i] += 1
            else:
                cnt[i] = 1
            tree += 1

            while len(cnt) > 2:
                fruit = fruits[l]
                cnt[fruit] -= 1
                tree -= 1
                l += 1

                if not cnt[fruit]:
                    cnt.pop(fruit)
            
            ans = max(ans, tree)
        return ans


