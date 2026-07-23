class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def getHours(x):
            hours = 0
            for p in piles:
                hours+= -((-p)//x)
            return hours

        l, r = 1, max(piles)
        while l<=r:
            mid = r+(l-r)//2
            hours=getHours(mid)
            if hours==h:
                r = mid-1
            elif hours>h:
                l=mid+1
            elif hours<h:
                r=mid-1
        return l

