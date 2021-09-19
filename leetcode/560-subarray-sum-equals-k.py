# https://leetcode.com/problems/subarray-sum-equals-k/

from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(lambda : 0)
        prefixSum = 0
        result = 0
        for num in nums:
            prefixSum += num
            complement = prefixSum - k
            
            # there will be some previous subarray to subtract from
            if complement in d:
                result += d[complement]
                
            # this case is exclusive to the previous case
            # since there is no previous subarray to subtract from
            if prefixSum == k: 
                result += 1
                
            d[prefixSum] += 1
        
        return result
        