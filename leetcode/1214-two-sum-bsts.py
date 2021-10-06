class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        
        mem1 = set()
        mem2 = set()
        
        def parse(root, isFirst):
            if not root:
                return
            
            if isFirst:
                mem1.add(root.val)
            else:
                mem2.add(root.val)
                
            parse(root.left, isFirst)
            parse(root.right, isFirst)
            
        parse(root1, True)
        parse(root2, False)
        
        for num in mem1:
            if target - num in mem2:
                return True
        
        return False
