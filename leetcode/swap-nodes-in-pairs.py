# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        curr = head
        toSwap = True
        while curr.next is not None:
            curr.val, curr.next.val = curr.next.val, curr.val
            if curr.next.next is not None:
                curr = curr.next.next
            else:
                return head
        return head