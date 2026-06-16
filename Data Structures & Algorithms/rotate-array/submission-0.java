class Solution {
    public void rotate(int[] nums, int k) {
        int tmp = 0;
        for (int count=0;count<k;count++){
            int l=0, r=nums.length-1;
            while(l<r){
                tmp=nums[l];
                nums[l]=nums[r];
                nums[r]=tmp;
                l+=1;
            }
        }
    }
}