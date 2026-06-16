class Solution {
    public int trap(int[] height) {
        int maxLeftValue = 0;
        int maxRightValue = 0;
        int[] maxLeft = new int[height.length];
        int[] maxRight = new int[height.length];
        // get every index's max on left and right
        for(int i=0;i<height.length;i++){
            if(i==0){
                maxLeft[i] = 0;
                continue;
            }
            maxLeftValue = Math.max(maxLeftValue, height[i-1]);
            maxLeft[i] = maxLeftValue;
        }
        for(int i=height.length-1;i>=0;i--){
            if(i==(height.length-1)){
                maxRight[i] = 0;
                continue;
            }
            maxRightValue = Math.max(maxRightValue, height[i+1]);
            maxRight[i] = maxRightValue;
        }
        // cal every index's area
        int res = 0;
        for(int i=0;i<height.length;i++){
            int newArea = Math.min(maxLeft[i], maxRight[i])-height[i];
            if( newArea>0 ){
                res+=newArea;
            }
        }
        return res;
    }
}
