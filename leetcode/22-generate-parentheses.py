class Solution:
    
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def recursion(leftRemains, rightRemains, current):
            if leftRemains > rightRemains or leftRemains < 0 or rightRemains < 0:
                return
            if leftRemains == 0 and rightRemains == 0:
                ans.append(current)
                return
            recursion(leftRemains-1, rightRemains, current+'(')
            recursion(leftRemains, rightRemains-1, current+')')
        
        recursion(n,n,'')
        
        return ans