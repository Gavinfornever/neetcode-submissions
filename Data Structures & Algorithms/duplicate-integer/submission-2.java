
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numsSet = new HashSet<>();
        for (int x=0; x< nums.length;x++){
            Boolean res = numsSet.add(nums[x]);
            if(res==false){
                return true;
            }
        }
        return false;
    }
}