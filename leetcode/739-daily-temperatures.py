# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0 for _ in range(len(temperatures))]
        stack = []
        
        for i, temperature in enumerate(temperatures):
            while stack and stack[-1][1] < temperature:
                result[stack[-1][0]] = i - stack[-1][0]
                stack.pop()
            stack.append((i, temperature))
            
        return result