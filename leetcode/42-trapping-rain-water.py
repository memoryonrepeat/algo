# https://leetcode.com/problems/trapping-rain-water/

from collections import deque

class Solution:
    def trap(self, height: List[int]) -> int:
        maxFromLeft = -float("inf")
        maxFromRight = -float("inf")
        ans = 0
        leftHeights = []
        rightHeights = deque([])
        for i in range(len(height)):
            maxFromLeft = max(maxFromLeft, height[i])
            maxFromRight = max(maxFromRight, height[len(height)-i-1])
            leftHeights.append(maxFromLeft)
            rightHeights.appendleft(maxFromRight)
        for i in range(len(height)):
            ans += min(leftHeights[i], rightHeights[i]) - height[i]
        return ans