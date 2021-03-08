# https://leetcode.com/problems/strobogrammatic-number/

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        matches = {'6': '9', '1': '1', '8': '8', '0': '0', '9': '6'}
        i = 0
        while i<len(num)/2:
            j = len(num)-1-i
            if num[i] not in matches or matches[num[i]] != num[j]:
                return False
            i += 1
        return True