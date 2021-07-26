class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        unique = set()
        fingerprint = [0 for _ in range(len(candidates))]
        
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