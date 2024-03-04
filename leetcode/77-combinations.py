class Solution:
    def __init__(self):
        self.ans = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = [i for i in range(1,n+1)]

        def backtrack(candidates,k,current):
            if k==0:
                self.ans += [current]
                return
            for i,candidate in enumerate(candidates):
                backtrack(candidates[i+1:], k-1, current + [candidate])

        backtrack(candidates,k,[])

        return self.ans