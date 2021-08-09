# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(s) <= 1:
            return s
        i = 0
        while i<len(s):
            while i<len(s)-1 and s[i] == s[i+1]:
                s = self.removeDuplicates(s[:i]+s[i+2:])
                i = 0
            i += 1
                
        return s