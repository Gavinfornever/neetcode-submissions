class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<=1:return 0
        l,r = 0,1
        mx = 0
        while r < len(prices):
            if prices[r]<prices[l]:
                l = r
            else:
                mx  = max(prices[r]-prices[l], mx)
            r+=1
        
        return mx