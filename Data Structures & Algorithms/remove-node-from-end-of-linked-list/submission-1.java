/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverse(ListNode head){
        ListNode p1=null, p2=head;
        while(p2!=null){
            ListNode temp = p2.next;
            p2.next = p1;
            p1=p2;
            p2=temp;
        }
        return p1;
    }
    public ListNode removeNthFromEnd(ListNode head, int n) {
        head = reverse(head);
        if(head.next==null && (n==1) )return null;
        ListNode p1=head, p2=head.next;
        if(n==1){
            head = head.next;
        }else{
            while( (n-1) > 1){
                p1 = p1.next;
                p2 = p2.next;
                n--;
            }
            p1.next = p2.next;
        }
        head = reverse(head);
        return head;
    }
}
