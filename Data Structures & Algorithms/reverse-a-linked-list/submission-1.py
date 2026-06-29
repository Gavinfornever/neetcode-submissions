# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def p(head):
            x = head
            while x.next:
                print(x.val)
                x = x.next
        # a -> b -> c -> d
        # l    r
        #      l    r
        if head is None: return None
        if head.next == None:
            return None

        last = None
        l, r = head, head.next
        while r:
            print("l, r:", l.val, r.val)
            tmp = r.next
            r.next = l
            l.next = last
            last = l

            p(r)

            l = r
            # tmp = r.next
            r = tmp
            
        
        return l

        # a -> b <- c <- d
        # b, c, d
        # d.next = c
        # c.next = b

