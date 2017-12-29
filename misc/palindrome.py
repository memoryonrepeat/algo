# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(e for e in s if e.isalnum()).lower()
        return s == s[::-1]