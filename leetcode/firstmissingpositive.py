# https://leetcode.com/problems/first-missing-positive/
class Solution:
    # Find smallest positive int that is not the array
    def firstMissingPositive(self, nums: List[int]) -> int:
        table = {}
        result = 1
        for num in nums:
            if num not in table:
                table[num] = True
        while result in table:
            result += 1
        return result
        