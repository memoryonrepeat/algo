class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        nums = [lower-1] + nums
        nums += [upper+1]
        for i in range(len(nums)-1):
            if nums[i]+1 <= nums[i+1]-1:
                result += [[nums[i]+1, nums[i+1]-1]]
        return result