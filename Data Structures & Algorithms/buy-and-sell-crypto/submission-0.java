class Solution {
    public int maxProfit(int[] prices) {
        int l=0,r=1;
        int max=0;
        if(prices.length==1)return 0;
        while(r<prices.length){
            if(prices[l]>prices[r]){
                l=r;
                r+=1;
            }else if(prices[l]==prices[r]){
                r+=1;
            }else{
                max=Math.max(max, prices[r]-prices[l]);
                r+=1;
            }
        }
        return max;
    }
}
