class Solution {
    public int[] productExceptSelf(int[] nums) {
        int productOfAll = 1;
        for(int num: nums){
            productOfAll = productOfAll * num;
        }
        int[] res = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            if(nums[i]==0){
                int tmp = 1;
                for(int j=0;j<nums.length;j++){
                    if(j!=i){
                        tmp = tmp*nums[j];
                    }
                }
                res[i] = tmp;
                continue;
            }
            res[i] = productOfAll / nums[i];
        }
        return res;
    }
}  
