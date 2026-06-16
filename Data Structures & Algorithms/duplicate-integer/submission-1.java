class Solution {
    public boolean hasDuplicate(int[] nums) {
        for(int x=0; x< nums.length; x++){
            for(int y=0; y<nums.length; y++){
                if(x == y){
                    continue;
                }
                if(nums[x] == nums[y]){
                    return true;
                }
            }
        }
        return false;
    }
}