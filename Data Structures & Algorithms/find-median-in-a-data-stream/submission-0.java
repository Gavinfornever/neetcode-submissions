
public class MedianFinder {

    private Queue<Integer> small;
    private Queue<Integer> large;

    public MedianFinder() {
        small = new PriorityQueue<Integer>((a, b)->b-a);
        large = new PriorityQueue<Integer>((a, b)->a-b);
    }
    
    public void addNum(int num) {
        small.add(num);
        if(small.size()-large.size()>1 || !large.isEmpty() && small.peek()>large.peek()){
            large.add(small.poll());
        }
        if(large.size()-small.size()>1){
            small.add(large.poll());
        }
    }
    
    public double findMedian() {
        if(small.size()==large.size()){
            return (double) (small.peek()+large.peek())/2.0;
        }else if(small.size()>large.size()){
            return (double) small.peek();
        }else{
            return (double) large.peek();
        }
    }
}