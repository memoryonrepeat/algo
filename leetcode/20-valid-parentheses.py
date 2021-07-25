# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'{': '}', '[': ']', '(': ')'}
        stack = []
        for char in s:
            if char in mp:
                stack.append(char)
            else:
                if not stack:
                    return False
                current = stack.pop()
                if char != mp[current]:
                    return False
        return len(stack) == 0