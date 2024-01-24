# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def getNumber(l, current):
            if not l.next:
                return int(str(l.val) + current)
            return getNumber(l.next, str(l.val)+current)

        result = getNumber(l1,"") + getNumber(l2, "")

        first = ListNode(result%10)
        last = first

        while result > 9:
            result = result // 10
            last.next = ListNode(result%10)
            last = last.next

        return first

