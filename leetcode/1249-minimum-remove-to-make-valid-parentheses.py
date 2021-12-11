# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        opens = []
        result = ''
        for i,c in enumerate(s):
            if c != '(' and c != ')':
                result += c
            elif c == '(':
                result += c
                opens += [len(result)-1]
            elif c == ')':
                if opens:
                    result += c
                    opens.pop()
        if opens:
            result = ''.join([result[i] for i,r in enumerate(result) if i not in opens])
        return result
        