# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        
        def backtrack(k,n,path,startFrom):
            if k == 0 and n == 0:
                ans.append(path[:])
                return
            if k < 0 or n < 0:
                return
            for i in range(startFrom, 10):
                path.append(i)
                backtrack(k-1,n-i,path,i+1)
                path.remove(i)
            
        backtrack(k,n,[],1)
        
        return ans