public class Solution {
    public ListNode reverse(ListNode head){
        ListNode p1=null,p2=head;
        while(p2!=null){
            ListNode tmp=p2.next;
            p2.next=p1;
            p1=p2;
            p2=tmp;
        }
        return p1;
    }
    public ListNode merge(ListNode p1, ListNode p2){
        ListNode p = new ListNode();
        ListNode head = p;
        System.out.println("---++---");
        print(p1);
        print(p2);
        System.out.println("---++---");
        while(p2!=null) {
            p.next = p1;
            p1 = p1.next;
            p = p.next;

            p.next = p2;
            p2 = p2.next;
            p = p.next;

        }
        System.out.println("------");
        print(p1);
        if(p1!=null){
            p.next = p1;
            p1 = p1.next;
            p = p.next;
            p.next=null;
        }
//        print(p2);
        print(head.next);
        System.out.println("------");
//        if(p1.next!=null){
//            p.next=p1.next;
//        }
        return head.next;
    }
    public void print(ListNode head){
        while(head!=null){
            System.out.print(head.val + " ");
            head=head.next;
        }
        System.out.println();
        System.out.println();
    }
    public void reorderList(ListNode head) {
        ListNode p1=head, p2=head;
        //find length and middle
        int length = 0;
        while(p1 !=null){
            length++;
            p1 = p1.next;
        }
        p1=head;
        //get p2 to the head of second half
        int step = (length+1)/2;
        System.out.println(step);
        while(step>0){
            p2 = p2.next;
            step--;
        }
        System.out.println("12321321");
        print(p2);
        //reverse the second half
        p2 = reverse(p2);
        print(p1);
        print(p2);
        //merge two halves
        ListNode res = merge(p1,p2);
        print(res);
        p1=res;
    }
}
