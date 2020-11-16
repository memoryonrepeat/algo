# https://leetcode.com/problems/group-anagrams/submissions/
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for word in strs:
            chars = tuple(sorted(word))
            if chars not in table:
                table[chars] = [word]
            else:
                table[chars].append(word)
        return table.values()