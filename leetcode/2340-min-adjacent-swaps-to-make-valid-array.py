class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        swaps = 0
        largest = max(nums)
        smallest = min(nums)
        largestPos = len(nums) - 1 - nums[::-1].index(largest)
        smallestPos = nums.index(smallest)
        largestMoves = len(nums) - 1 - largestPos
        smallestMoves = smallestPos
        if largestPos < smallestPos:
            return largestMoves + smallestMoves - 1
        return largestMoves + smallestMoves