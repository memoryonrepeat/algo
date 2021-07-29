# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        ans = []
        
        def recursion(head):
            if not head:
                return
            recursion(head.getNext())
            val = head.printValue()
            ans.append(val)
            return
        
        recursion(head)
            
        return ans
