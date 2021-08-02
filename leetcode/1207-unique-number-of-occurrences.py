# https://leetcode.com/problems/unique-number-of-occurrences/

from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        values = set()
        for value in c.values():
            if value not in values:
                values.add(value)
            else:
                return False
        return True