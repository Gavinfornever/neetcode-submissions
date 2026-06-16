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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode resList = new ListNode();
        ListNode cur = resList;
        int carry=0, val1=0, val2=0;
        while((l1!=null)||(l2!=null)||(carry!=0)){
            if(l1!=null)val1=l1.val;
            else val1=0;
            if(l2!=null)val2=l2.val;
            else val2=0;

            int sum = val1 + val2 + carry;
            carry = sum / 10;
            sum = sum % 10;
            cur.next = new ListNode(sum);
            
            cur = cur.next;
            l1 = (l1!=null)?l1.next:null;
            l2 = (l2!=null)?l2.next:null;
        }
        return resList.next;
        
        // ListNode x = l1, y = l2;
        // int push=0;
        // int which = 1;
        // while( (x!=null)||(y!=null)){
        //     if((x==null)&&(y!=null)){
        //         which = 2;
        //         int sum = y.val + push;
        //         push = 0;
        //         if(sum<10){
        //             y.val = sum;
        //         }else{
        //             ListNode tail = new ListNode(1);
        //             y.val = sum%10;
        //             y.next = tail;
        //             y = y.next;
        //             push = 1;
        //         }
        //         continue;
        //     }
        //     if((y==null)&&(x!=null)){
        //         which = 1;
        //         int sum = x.val + push;
        //         push = 0;
        //         if(sum<10){
        //             x.val = sum;
        //         }else{
        //             ListNode tail = new ListNode(1);
        //             x.val = sum%10;
        //             x.next = tail;
        //             push = 1;
        //             x = x.next;
        //         }
        //         continue;
        //     }

        //     int sum = x.val + y.val + push;
        //     push = 0; // reset
        //     if(sum<10){
        //         x.val = sum;
        //         y.val = sum;
        //     }else{
        //         x.val = sum%10;
        //         y.val = sum%10;
        //         push = 1;
        //     }
        //     if((x.next==null)&&(y.next==null)){
        //         if(push==1){
        //             ListNode tail = new ListNode();
        //             tail.val = 1;
        //             x.next = tail;
        //         }
        //         return l1;
        //     }
        //     x = x.next;
        //     y = y.next;
        // }
        // if(which == 1)return l1;
        // else return l2;
    }
}
