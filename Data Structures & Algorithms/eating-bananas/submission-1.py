class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = r
        while l<=r:
            m = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/m)
            if hours>h: # need higher speed
                l = m+1
            else: # can use slower speed
                minK = min(minK, m)
                r = m-1
        return minK
            
