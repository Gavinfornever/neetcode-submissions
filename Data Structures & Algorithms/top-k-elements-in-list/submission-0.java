class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //分类，得到每个数的出现次数的hashmap
        //进行快速排序，根据数的次数
        Map<Integer, Integer> map = new HashMap<>();
        for(int num : nums){
            int count = map.getOrDefault(num, 0);
            map.put(num, count+1);
        }
        //定义优先队列及其比较器
        //采用小根堆，因为堆只能保证每次取最小的，但是大的那些不要求有顺序，因为他的结构决定
        PriorityQueue<int[]> q = new PriorityQueue<int[]>(
            new Comparator<int[]>(){
                public int compare(int[] m, int[] n){
                    return m[1] - n[1];
                }
            }
        );
        //使用优先队列（堆）来对每个map中的进行排序
        //由于是小根堆，每次只对第一个元素操作
        for (Map.Entry<Integer, Integer> entry: map.entrySet()){
            int num = entry.getKey(), count = entry.getValue();
            if (q.size() == k){
                if(q.peek()[1] < count){
                    q.poll();
                    q.offer(new int[]{num, count});
                }
            }else{
                q.offer(new int[]{num, count});
            }
        }
        //得到了最终的队列，进行输出即可
        int[] res = new int[k];
        for (int i=0;i<k;i++){
            res[i] = q.poll()[0];
        }
        return res;
    }
}
