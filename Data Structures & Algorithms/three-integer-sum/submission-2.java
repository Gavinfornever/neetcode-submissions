class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();
        for(int i=0;i<nums.length;i++){
            int j=i+1, k=nums.length-1;
            if(i>0 && nums[i-1]==nums[i])continue;
            while(j<k){
                int sum = nums[i]+nums[j]+nums[k];
                if(sum>0){
                    k-=1;
                }else if(sum<0){
                    j+=1;
                }else{
                    List<Integer> list = new ArrayList<>();
                    list.add(nums[i]);
                    list.add(nums[j]);
                    list.add(nums[k]);
                    res.add(list);
                    j+=1;
                    while(nums[j]==nums[j-1]&&j<k){
                        j+=1;
                    }
                }
            }
        }
        return res;
    }
}
