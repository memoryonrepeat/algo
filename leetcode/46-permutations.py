class Solution:
    def __init__(self):
        self.result = []
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(pool, current):
            if not pool:
                self.result += [current]
                return
            for i, num in enumerate(pool):
                backtrack(pool[:i]+pool[i+1:], current+[num])
            
        backtrack(nums, [])
        
        return self.result