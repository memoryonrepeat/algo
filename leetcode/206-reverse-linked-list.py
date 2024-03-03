# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def _reverse(self, current, previous):
            if not current:
                return previous
            originalNext = current.next
            current.next = previous
            return self._reverse(originalNext, current)

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self._reverse(head, None)
