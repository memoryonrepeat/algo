# https://leetcode.com/problems/3sum/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        total = 0
        table = {}
        result = set()
        for num in nums:
            if num not in table:
                table[num] = 1
            else:
                table[num] += 1
        for key1 in table:
            table[key1] -= 1
            for key2 in table:
                if table[key2] == 0:
                    continue
                table[key2] -= 1
                key3 = total - key1 - key2
                if key3 in table and table[key3] > 0:
                    new = tuple(sorted([key1, key2, total - key1 - key2]))
                    result.add(new)
                table[key2] += 1
            table[key1] += 1
        return result
            
        
        
