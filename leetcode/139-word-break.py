class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(maxsize=None)
        def dp(s):
            if not s:
                return False
            if s in wordDict:
                return True
            for i in range(len(s)):
                if s[:i] in wordDict:
                    if dp(s[i:]):
                        return True
            return False

        return dp(s)
