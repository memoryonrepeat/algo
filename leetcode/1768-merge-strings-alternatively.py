class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        remaining = ""
        if len(word1) > len(word2):
            remaining = word1[len(word2):]
        elif len(word2) > len(word1):
            remaining = word2[len(word1):]
        return "".join([a+b for a,b in zip(word1, word2)]) + remaining