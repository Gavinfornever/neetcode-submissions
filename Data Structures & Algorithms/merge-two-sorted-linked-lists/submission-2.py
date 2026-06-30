# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h = ListNode()
        l = list1
        r = list2
        flag = False

        if not l:return r
        if not r:return l

        while l and r:
            if l.val<=r.val:
                if not flag:
                    h = l
                    flag = True

                tmp = l.next
                if l.next and l.next.val<=r.val:
                    l.next = r
                l = tmp
            else:
                if not flag:
                    h = r
                    flag = True

                tmp = r.next
                if r.next and r.next.val<=l.val:
                    r.next = l
                r = tmp
            
        return h

