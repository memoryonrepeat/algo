class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        if not t:
            return not s
        pos = t.find(s[0])
        if pos == -1:
            return False
        return self.isSubsequence(s[1:], t[pos+1:])
        