class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(cap):
            days=1
            cur=0
            for w in weights:
                if cur+w>cap:
                    days+=1
                    cur=w
                else:
                    cur+=w
            return days
        
        l,r=max(weights),sum(weights)+1
        while l<r:
            m=r+(l-r)//2
            ds = check(m)
            if ds>days:
                l=m+1
            elif ds<=days:
                r=m
        return l

