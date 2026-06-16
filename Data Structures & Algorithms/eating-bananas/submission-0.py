class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minm = r
        def getHours(rate):
            res = 0
            for pile in piles:
                res += math.ceil(pile/rate)
            return res
        
        while l<=r:
            m = (l+r)//2
            hours = getHours(m)
            if hours > h:
                l = m + 1
            elif hours <= h:
                r = m - 1
                minm = min(minm, m)
            
        return minm
