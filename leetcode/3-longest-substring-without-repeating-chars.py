# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        index = {}
        current = s[left:right]
        longest = len(current)
        while right < len(s):
            currentChar = s[right]
            if currentChar in index and index[currentChar] >= left:
                left = index[currentChar]+1
            index[currentChar] = right
            right += 1
            current = s[left:right]
            longest = max(longest, len(current))
        return longest

# Redo 25/2/24            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxLength = 0
        current = ""
        
        while i < len(s):
            if s[i] not in current:
                current += s[i]
                i += 1
            else:
                maxLength = max(maxLength, len(current))
                i = i - len(current) + current.index(s[i]) + 1
                current = ""
            
        maxLength = max(maxLength, len(current))
        
        return maxLength