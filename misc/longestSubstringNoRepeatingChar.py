# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# TODO:
# - Only saves the length as problem does not require whole substring
# - Use hash table / counter to remember the count of each character in current substring and modify accordingly after each loop

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 1
        longest = s[start:end]
        current = s[start:end]
        while(end<len(s)):
            # print(start,end,s,s[end],current)
            if s[end] in current:
                # print('Y',start,end,s,s[end],current)
                start = s.rfind(s[end],0,end)+1
            end += 1
            current = s[start:end]
            # print(start,end,current)
            if len(current)>len(longest):
                longest = current
                # print('S',longest,current)
        return len(longest)
                
        