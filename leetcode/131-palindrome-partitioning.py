class Solution:
    def __init__(self):
        self.ans = []

    def isPalindrome(self, s):
        return len(s)>0 and s == s[::-1]
    
    def backtrack(self, s, current):
        if not s:
            if current:
                self.ans.append(current)
                return
        if len(s) == 1:
            current += [s]
            self.ans.append(current)
            return
        for i in range(len(s)):
            if self.isPalindrome(s[:i+1]):
                self.backtrack(s[i+1:], current + [s[:i+1]])

    def partition(self, s: str) -> List[List[str]]:
        self.backtrack(s, [])

        return self.ans