# https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, a): 
        size = len(a)
        max_so_far =a[0] 
        curr_max = a[0] 

        # Idea: If a subarray sums to a negative number, it's not worth keeping
        for i in range(1,size):
            curr_max = max(a[i], curr_max + a[i]) 
            max_so_far = max(max_so_far,curr_max) 

        return max_so_far 
