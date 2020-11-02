# https://leetcode.com/problems/subdomain-visit-count/
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            subs = domain.split(".")
            for i in range(0, len(subs)):
                current_sub = ".".join(subs[i:])
                print(current_sub)
                if current_sub in res:
                    res[current_sub] += int(count)
                else:
                    res[current_sub] = int(count)
        output = []
        for key in res:
            output.append('{} {}'.format(res[key], key))
        return output
                    
                
                
            