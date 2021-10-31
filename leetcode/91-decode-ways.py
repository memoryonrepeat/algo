# https://leetcode.com/problems/decode-ways/

from functools import lru_cache

class Solution:
    nums = [str(i) for i in range(1, 27)]
    
    @lru_cache(maxsize = None)
    def numDecodings(self, s: str) -> int:
        if not s:
            return 1
        if s[0] == '0':
            return 0
        ans = self.numDecodings(s[1:])
        if len(s)>=2 and s[:2] in self.nums:
            ans += self.numDecodings(s[2:])
        
        return ans