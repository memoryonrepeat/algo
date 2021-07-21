# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i = 0
        result = ''
        currentChar = None
        while i<len(strs[0]):
            for s in strs:
                if i>=len(s):
                    return result
                if not currentChar:
                    currentChar = s[i]
                else:
                    if s[i] != currentChar:
                        return result
            result += strs[0][i]
            i += 1
            if i < len(strs[0]):
                currentChar = strs[0][i]
        return result