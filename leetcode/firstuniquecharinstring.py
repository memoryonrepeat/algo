# https://leetcode.com/problems/first-unique-character-in-a-string/

from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        c = Counter(s)
        _min = len(s)
        for k in c:
            if c[k] == 1:
                _min = min(_min, s.index(k))
        return -1 if _min == len(s) else _min