# https://leetcode.com/problems/partition-array-into-disjoint-intervals/

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        maxLeft = nums[left]
        minRight = nums[right]
        while left < right:
            if maxLeft <= minRight:
                right -= 1
                minRight = min(minRight, nums[right])
            else:
                maxLeft = max(nums[left:right])
                while maxLeft > minRight:
                    right += 1
                    minRight = min(nums[right:])
                return right
        return right+1