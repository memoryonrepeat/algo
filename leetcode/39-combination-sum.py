# https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        # Set of unique fingerprints aka unique solutions
        unique = set()
        
        # Count of each number in current solution, to differentiate with others
        fingerprint = [0 for _ in range(len(candidates))]
        
        # When backtracking, keep a fingerprint string to check for duplicate solutions
        def backtrack(candidates, target, current, fingerprint):
            if target == 0:
                fingerprintString = ','.join(str(c) for c in fingerprint)

                if fingerprintString not in unique:
                    ans.append(current[:])
                    unique.add(fingerprintString)
                return

            for i,candidate in enumerate(candidates):
                if candidate <= target:
                    current.append(candidate)
                    fingerprint[i] += 1
                    backtrack(candidates, target - candidate, current, fingerprint)
                    current.remove(candidate)
                    fingerprint[i] -= 1
                    
        backtrack(candidates, target, [], fingerprint)
        
        return ans

# Redo 3/1/024
# Instead of keeping track of uniqueness using set + fingerprint, use incremental index
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(target, current, start):
            if target == 0:
                ans.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    current.append(candidates[i])
                    backtrack(target - candidates[i], current, i) # current index might still be reused
                    current.remove(candidates[i])
                    
        backtrack(target, [], 0)
        
        return ans

# Redo 28/2/24
# Instead of backtracking in between adding / removing candidate, just put updated candidate as parameter
# Feels more natural and less mental overhead since no need to manually keep track of adding / removing
# thanks to the closure nature of recursion call (updated param of one call does not affect other calls)
# Can be used as a template as well.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        
        def backtrack(target, current, start):
            if target == 0:
                ans.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    backtrack(target - candidates[i], current + [candidates[i]], i)
                    
        backtrack(target, [], 0)
        
        return ans