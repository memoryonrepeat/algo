# https://leetcode.com/problems/single-row-keyboard/

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        table = {}
        for i in range(len(keyboard)):
            table[keyboard[i]] = i
        result = 0
        current = 0
        for w in word:
            result += abs(table[w]-current)
            current = table[w]
        return result