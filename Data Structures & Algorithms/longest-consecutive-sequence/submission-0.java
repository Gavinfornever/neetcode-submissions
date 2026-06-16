class Solution {
    public int longestConsecutive(int[] nums) {
        //Map<Integer, List<Integer>> map = new HashMap<Integer, List<Integer>>();
        //首先找到可以作为头的数字，注意不能on^2的方式，一个数对比一圈，而是用set的特性，分为两步得到这样的数字
        //得到以后，对每个数字进行数组长度的累积，甚至不用存下来这个数组
        Set<Integer> set = new HashSet<>();
        for (int num: nums){
            set.add(num);
        }
        int longest = 0;
        for (int num: nums){
            if(!set.contains(num-1)){//如果不存在就可以是头，因为不是每个都是头，所以复杂度并非n^2，最坏
                int len =  1;
                while(set.contains(num + len)){
                    len++;
                }
                longest = Math.max(len, longest);
            }
        }
        return longest;

    }
}
