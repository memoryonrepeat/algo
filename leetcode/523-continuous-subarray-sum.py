# https://leetcode.com/problems/continuous-subarray-sum/

from collections import defaultdict

# Idea: Prefix sum + two (modulo) sum
# Sum of continuous subarray = Difference between 2 prefix sums
# If the difference of both modulos is a multiple of k -> found
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2:
            return False
        modulo = defaultdict(set)
        prefixSum = 0
        for i, num in enumerate(nums):
            prefixSum += num
            currentMod = prefixSum % k
            if i>=1 and currentMod == 0 or (currentMod in modulo and modulo[currentMod] != {i-1}) or k + currentMod in modulo:
                return True
            modulo[currentMod].add(i)
        return False