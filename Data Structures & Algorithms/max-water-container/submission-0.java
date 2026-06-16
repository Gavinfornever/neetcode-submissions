class Solution {
    public int maxArea(int[] heights) {
        int l=0, r=heights.length-1;
        int max = -1;
        while(l<r){
            max = Math.max(Math.min(heights[l],heights[r])* (r-l), max) ;
            if(heights[l]<=heights[r]){
                l+=1;
            }else{
                r-=1;
            }
        }
        return max;
    }
}
