# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        x=h
        l = list1
        r = list2

        if not l:return r
        if not r:return l

        while l and r:
            if l.val<=r.val:
                x.next = l
                l = l.next
            else:
                x.next = r
                r = r.next
            x = x.next

        # if l:
        #     x.next = l
        # if r:
        x.next = l or r
            
        return h.next

