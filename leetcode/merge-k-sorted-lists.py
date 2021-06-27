# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# https://leetcode.com/problems/merge-k-sorted-lists/submissions/

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        lists = list(filter(None, lists))
        resultHead = resultTail = None
        while len(lists)>0:
            minIndex, minHead = min(enumerate(lists), key = lambda h: h[1].val)
            if resultHead:
                resultTail.next = ListNode(minHead.val)
                resultTail = resultTail.next
            else:
                resultHead = ListNode(minHead.val)
                resultTail = resultHead
            # print(minIndex, minHead, resultHead)
            lists[minIndex] = lists[minIndex].next
            lists = list(filter(None, lists))
        return resultHead