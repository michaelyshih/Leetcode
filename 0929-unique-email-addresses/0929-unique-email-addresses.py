from collections import defaultdict as d 
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        table = d(int)
        for email in emails: 
            [local, domain] = email.split("@")
            local = local.split("+")[0]
            local = "".join(local.split("."))
            email = "@".join([local, domain])
            table[email] += 1 
        return len(table.keys())
        