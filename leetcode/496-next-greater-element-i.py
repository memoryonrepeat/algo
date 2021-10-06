# https://leetcode.com/problems/next-greater-element-i/

# Idea: Build a decreasing stack, when facing a non-decreasing number, 
# keep popping until stack is decreasing again --> that number is the next greater number
# for popped elements

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = {}
        
        stack = []
        
        for num in nums2:
            while stack and stack[-1] < num:
                result[stack[-1]] = num
                stack.pop()
            stack.append(num)
            
        for num in stack:
            result[num] = -1
        
        return list(map(lambda e: result[e], nums1))