# https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:
            return False
        
        mem = {}
        
        def dp(current, lastJump):
            # print(current, lastJump, mem)
            if current == stones[-1]:
                return True
            if (current, lastJump) in mem:
                return mem[(current, lastJump)]
            for j in [lastJump-1, lastJump, lastJump+1]:
                if j>0 and current+j in stones and dp(current+j, j):
                    mem[(current, lastJump)] = True
                    return True
            mem[(current, lastJump)] = False
            return False
        
        return dp(1,1)
        