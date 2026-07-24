class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def getDays(cap:int) -> int:
            days=1
            cur = 0
            for w in weights:
                if cur+w>cap:
                    days+=1
                    cur=w
                else:
                    cur+=w
            return days
            
        l,r=max(weights),sum(weights)
        while l<=r:
            m=r+(l-r)//2
            ds = getDays(m)
            if ds==days:
                return m
            elif ds<days:
                r=m-1
            elif ds>days:
                l=m+1
        
        # if getDays(l-1)>=days:
        #     return l-1

        return l


