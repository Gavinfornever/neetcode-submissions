# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        m = l1
        n = l2
        x = head = ListNode()
        carry = 0
        while m or n or (carry!=0):
            m_val = m.val if m else 0
            n_val = n.val if n else 0
            _sum = m_val + n_val + carry
            carry = _sum // 10
            _sum = _sum % 10
            tmpNode = ListNode(_sum)
            x.next=tmpNode
            x = x.next
            m = m.next if m else None
            n = n.next if n else None
        return head.next