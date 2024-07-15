# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        if list1.val <= list2.val:
            return ListNode(list1.val, self.mergeTwoLists(list1.next, list2))
        return ListNode(list2.val, self.mergeTwoLists(list1, list2.next))
        
# Redo 15/7 - Imperative
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode(None, None)
        head = tail
        while True:
            if not list1:
                tail.next = list2
                break
            if not list2:
                tail.next = list1
                break
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next       
            tail = tail.next
        return head.next
            
        