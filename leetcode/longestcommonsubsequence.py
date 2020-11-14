# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.dp(text1, text2, {})
    
    def dp(self, text1: str, text2: str, table) -> int:
        if len(text1) == 0 or len(text2) == 0:
            table[(len(text1), len(text2))] = 0
            return 0
        if (len(text1), len(text2)) in table:
            return table[(len(text1), len(text2))]
        if text1[0] == text2[0]:
            local_result = 1+self.dp(text1[1:], text2[1:], table)
            table[(len(text1), len(text2))] = local_result
            return local_result
        local_result = max(self.dp(text1, text2[1:], table), self.dp(text1[1:], text2, table))
        table[(len(text1), len(text2))] = local_result
        return local_result