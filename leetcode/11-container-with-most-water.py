class Solution:
    
    def maxArea(self, height: List[int]) -> int:
        lower = min(height[0], height[-1])
        left = 0
        right = len(height)-1
        result = (len(height)-1)*lower
        while left < right:
            result = max(result, (right - left)*min(height[left], height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result