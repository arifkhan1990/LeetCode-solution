class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = []
        for i in emails:
            domian = i[i.find('@'):]
            local = i[:i.index('@')]
            if '+' in local:
                local = local[:local.find('+')]
            local = local.replace('.','')
            ans.append(local+domian)

        return len(set(ans))
