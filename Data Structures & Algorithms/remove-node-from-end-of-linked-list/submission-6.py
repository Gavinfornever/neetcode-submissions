# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def reverse(p):
            prev, cur = None, p
            while cur:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev
        
        head = reverse(head)

        count = 0
        prev = None
        cur = head
        while count<n-1:
            prev = cur
            cur = cur.next
            count+=1

        if not prev:
            head = head.next
        else:
            if cur:
                prev.next = cur.next
                cur.next = None
            else:
                prev.next = None

        head = reverse(head)

        return head