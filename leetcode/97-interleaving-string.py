class Solution:

    @lru_cache(maxsize=None)
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3
        if not s2:
            return s1 == s3
        if not s3:
            return False
        if s3[0] != s1[0] and s3[0] != s2[0]:
            return False
        if s3[0] == s1[0]:
            if s3[0] == s2[0]:
                return self.isInterleave(s1[1:], s2, s3[1:]) or self.isInterleave(s1, s2[1:], s3[1:])
            else:
                return self.isInterleave(s1[1:], s2, s3[1:])
        elif s3[0] == s2[0]:
            return self.isInterleave(s1, s2[1:], s3[1:])
        return False