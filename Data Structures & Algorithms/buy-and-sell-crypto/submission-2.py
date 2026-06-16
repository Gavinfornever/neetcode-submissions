class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:return 0
        l, r = 0, 0
        maxP = -1
        while(r<len(prices)):
            if (prices[l]>prices[r]):
                l = r
                r +=1
            else:
                maxP = max(maxP, prices[r]-prices[l])
                r+=1
        return maxP
