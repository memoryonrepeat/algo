# https://leetcode.com/problems/edit-distance/

class Solution:
    dp = None
    
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1)
        l2 = len(word2)
        
        if not self.dp:
            self.dp = [[None for i in range(l2+1)] for j in range(l1+1)]
        
        if self.dp[l1][l2]:
            return self.dp[l1][l2]
        
        if l1 == 0 or l2 == 0:
            self.dp[l1][l2] = max(l1,l2)
            return self.dp[l1][l2]
        
        if word1[-1] == word2[-1]:
            self.dp[l1][l2] = 1 + min(self.minDistance(word1[:-1], word2[:-1])-1, self.minDistance(word1[:-1], word2), self.minDistance(word1, word2[:-1]))
        else:
            self.dp[l1][l2] = 1 + min(self.minDistance(word1[:-1], word2[:-1]), self.minDistance(word1[:-1], word2), self.minDistance(word1, word2[:-1]))
        
        return self.dp[l1][l2]
            
        
        