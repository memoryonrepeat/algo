from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)
        for c in rCounter:
            if c not in mCounter or rCounter[c] > mCounter[c]:
                return False
        return True
            