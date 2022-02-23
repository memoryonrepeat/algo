# https://leetcode.com/problems/lexicographical-numbers/

from functools import cmp_to_key

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        l = [i for i in range(1,n+1)]
        return sorted(l, key = cmp_to_key(lambda a,b: 1 if str(a) > str(b) else -1))