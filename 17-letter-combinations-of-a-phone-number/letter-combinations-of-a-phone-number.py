class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        
        keyboard = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        def solve(idx, digits, keyboard, subset):
            if idx == len(digits):
                if len(subset) != 0:
                    ans.append(''.join(subset[:]))
                return
            
            keys = keyboard[int(digits[idx])]

            for i in keys:
                subset.append(i)
                solve(idx+1, digits, keyboard, subset)
                subset.pop()
        solve(0,digits, keyboard, [])
        return ans