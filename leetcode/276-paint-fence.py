from functools import lru_cache

class Solution:

    @lru_cache(maxsize=None)
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k*k
        return (k-1)*self.numWays(n-1,k) + (k-1)*self.numWays(n-2,k)
        