class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        typei = []
        colori = []
        namei = []
        
        ans = 0
        for item in items:
                typei.append(item[0])
                colori.append(item[1])
                namei.append(item[2])
        if ruleKey == "type":
            ans = typei.count(ruleValue)
        elif ruleKey == "color":
            ans = colori.count(ruleValue)
        else:
            ans = namei.count(ruleValue)
        return ans