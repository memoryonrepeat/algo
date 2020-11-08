# https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if num not in table:
                table[num] = i
            if (target-num) in table and i != table[target-num]:
                return [i, table[target-num]]
        return []
        