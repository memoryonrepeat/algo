# https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(filter(lambda w: len(w)>0, s.strip().split(' ')[::-1]))