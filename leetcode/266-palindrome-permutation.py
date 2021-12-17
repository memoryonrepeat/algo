# https://leetcode.com/problems/palindrome-permutation/

from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = Counter(s)
        singles = 1 if len(s)%2 == 1 else 0
        for key in c:
            if c[key] % 2 == 1:
                singles -= 1
                if singles < 0:
                    return 0
        return True