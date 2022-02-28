# https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(s, prev):
            if not s:
                return False
            if int(s) == prev - 1:
                return True
            for i in range(len(s)):
                current = int(s[:i+1])
                if current == prev - 1 and backtrack(s[i+1:], current):
                    return True
            return False
            
        for i in range(len(s)):
            current = int(s[:i+1])
            if backtrack(s[i+1:], current):
                return True
            
        return False
        