class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(curr,toOpen,opened,res):
            if toOpen == 0 and opened == 0:
                res.append(curr)
                return
            if toOpen > 0:
                dfs(curr+ "(",toOpen-1,opened + 1,res)
            if opened > 0:
                dfs(curr + ")",toOpen, opened-1,res)

        dfs("",n,0,res)
        return res