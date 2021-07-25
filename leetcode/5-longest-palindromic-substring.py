# https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        start = end = 0
        
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s), 1):
                dp[i][j] = s[i]==s[j] and (j-i<3 or dp[i+1][j-1])
                if dp[i][j] and end-start<j-i:
                    end = j
                    start = i
        return s[start:end+1]