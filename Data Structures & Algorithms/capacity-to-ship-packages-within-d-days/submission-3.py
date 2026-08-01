class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l,r=max(weights), sum(weights)+1
        
        def check(cap):
            days = 1
            cur = 0
            for w in weights:
                if w+cur>cap:
                    days+=1
                    cur=w
                else:
                    cur+=w
            return days
        
        while l<r:
            m=r+(l-r)//2
            ds = check(m)
            if days<ds:
                l=m+1
            elif days == ds:
                r=m
            elif days>ds:
                r=m

        return l
