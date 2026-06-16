class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 0
        res = 0
        # while (j<len(prices)):
        #     if (j+1)<len(prices) and prices[j+1]>=prices[j]:
        #         j+=1
        #     elif (j+1)<len(prices) and prices[j+1]<prices[j] and prices[i]<prices[j]:
        #         res+= (prices[j]-prices[i])
        #         i = j+1
        #         j = i+1
        #     elif (j+1)==len(prices):
        #         if prices[i]<prices[j]:
        #             res+= (prices[j]-prices[i])
        #         break
        #     else:
        #         j+=1
        while j<len(prices):
            if prices[i]<=prices[j]:
                if ((j+1)<len(prices) and prices[j+1]<prices[j]) or \
                   (j+1)==len(prices):
                    # get value
                    res+= prices[j]-prices[i]
                    i = j
                    j = i+1
                    continue
                j+=1
            else:
                i = j
                j = i+1

        return res