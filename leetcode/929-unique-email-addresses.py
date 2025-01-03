# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = {}
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.','')
            plus = local.find('+')
            if plus > -1:
                local = local[:plus]
            destination = local + '@' + domain
            uniqueEmails[destination] = True
        return len(uniqueEmails)