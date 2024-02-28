class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start, current):
            result.append(current[:])

            for i in range(start, len(nums)):
                backtrack(i+1, current+[nums[i]])

        backtrack(0,[])

        return result