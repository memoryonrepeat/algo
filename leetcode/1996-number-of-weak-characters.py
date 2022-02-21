# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        # sort by ascending attack
        # if same attack, sort defense descending to avoid double counting
        # since the ones with same attack are not eligible as weak characters
        # relatively to each other
        properties.sort(key = lambda p: (p[0], -p[1]))
        stack = []
        result = 0
        for attack, defense in properties:
            while stack and stack[-1] < defense:
                stack.pop()
                result += 1
            stack.append(defense)
        return result