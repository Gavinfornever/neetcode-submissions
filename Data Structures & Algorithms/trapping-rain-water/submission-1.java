class Solution {
    public int trap(int[] height) {
        int l=0, r=height.length-1;
        int maxLeft=0, maxRight=0;
        int res=0;
        while(l<=r){
            if(maxLeft<=maxRight){
                int area = maxLeft-height[l];
                if(area>0){
                    res+=area;
                }
                maxLeft = Math.max(maxLeft, height[l]);
                l++;
            }else{
                int area = maxRight-height[r];
                if(area>0){
                    res+=area;
                }
                maxRight = Math.max(maxRight, height[r]);
                r--;
            }
        }
        return res;
    }
}
