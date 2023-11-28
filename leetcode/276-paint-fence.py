# https://leetcode.com/problems/paint-fence/

from functools import lru_cache

class Solution:

    # Let f(i) = total ways for i fences (k is fixed)
    # f(1) = k
    # f(2) = k*k
    # Consider f(n). There are 2 ways:
    # Paint n with different color from n-1 --> (k-1)*f(n-1)
    # Paint n with the same color from n-1
    # --> Then n-2 must be of different color from n-1 --> (k-1)*f(n-2)
    @lru_cache(maxsize=None)
    def numWays(self, n: int, k: int) -> int:
        if n == 1:
            return k
        if n == 2:
            return k*k
        return (k-1)*self.numWays(n-1,k) + (k-1)*self.numWays(n-2,k)

    # Another way using state machine
    # https://leetcode.com/problems/paint-fence/solutions/913354/python-state-machine-solution/
    def numWays(self, n: int, k: int) -> int:
        if n < 2: 
            return n * k
        same, diff = 0, k
        for i in range(1, n):
            same, diff = diff, (k - 1) * (diff + same)
        return same + diff
        