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

# Redo 5/3/24
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = [0,0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n-1):
            dp[i][i+1] = (s[i] == s[i+1])
            ans = [i,i+1] if dp[i][i+1] else ans

        for diff in range(2,n):
            for i in range(n-diff):
                j = i+diff
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    ans = [i,j]

        return s[ans[0] : ans[1]+1]