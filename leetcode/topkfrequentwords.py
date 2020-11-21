# https://leetcode.com/problems/top-k-frequent-words/submissions/

from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        c = Counter(words)
        s = sorted(c.keys(), key = lambda w: (-c[w], w))
        return s[:k]