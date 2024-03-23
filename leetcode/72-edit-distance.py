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
            
# Redo 23/3/24
class Solution:
    @lru_cache(maxsize=None)
    def minDistance(self, word1: str, word2: str) -> int:
        if word1 == word2:
            return 0
        if not word1 or not word2:
            return max(len(word1), len(word2))
        if word1[0] == word2[0]:
            return 1 + min( self.minDistance(word1[1:], word2[1:])-1, self.minDistance(word1, word2[1:]), self.minDistance(word1[1:], word2))
        else:
            return 1 + min( self.minDistance(word1[1:], word2[1:]), self.minDistance(word1, word2[1:]), self.minDistance(word1[1:], word2))