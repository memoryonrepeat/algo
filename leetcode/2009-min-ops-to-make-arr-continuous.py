# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Idea:
        # The problem is equivalent to finding min operations
        # to map the original array into [k, k+1, ..., k+N-1] with N=length(nums)
        # --> Max number of operations = N (not optimal)
        # But we can skip those numbers that are already there in the sorted array
        # --> Those numbers will form a sorted discontinuous subarray
        # --> Min number of ops happens when we can find the longest sorted discontinuous subarray
        N = len(nums)
        queue = deque()
        target = sorted(set(nums))
        longest = 1

        for t in target:
            # Keep popping "impossible" numbers out of queue
            # "Impossible" numbers = numbers that are too small to be in final queue
            # Too small == gap between itself and next number > max allowed gap (N-1)
            while queue and (t-queue[0])>=N:
                queue.popleft()
            queue.append(t)
            longest = max(longest, len(queue))
        return N - longest