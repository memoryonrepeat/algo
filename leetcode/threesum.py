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
        
# Redo 3/3/24
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        seen = set()
        for i, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            candidates = self.twoSum(nums[i+1:], -num)
            if candidates:
                ans += list(map(lambda c: [num,c[0],c[1]], candidates))
        return ans

    def twoSum(self, nums, target):
        if not nums:
            return []
        seen = {}
        ans = set()
        for i,num in enumerate(nums):
            if num not in seen:
                seen[num] = i
            if target - num in seen and i != seen[target-num] :
                ans.add((num, target-num))
        return ans
        
            