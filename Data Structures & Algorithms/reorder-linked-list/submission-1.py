# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first, second = head, head.next
        while second and second.next:
            first  = first.next
            second = second.next.next
        second = first.next

        prev = first.next = None ####
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        # first, second

        first = head
        second = prev
        while second:
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2

        # dn = p = ListNode()
        # x, y = first, second
        # # while x and y:
        # while y:
        #     # p.next = x
        #     p = x
        #     x = x.next
        #     p.next = y
        #     p = y
        #     y = y.next
        # p.next = x


