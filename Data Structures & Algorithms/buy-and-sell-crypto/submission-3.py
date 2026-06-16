class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = -1
        l, r = 0, 0
        while(r<len(prices)):
            if prices[l]>prices[r]:
                l=r
                r+=1
            else:
                maxP = max(maxP, prices[r]-prices[l])
                r+=1
        return maxP

