class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        # 0 9 - 4
        # 
        while l<=r:
            m=r+(l-r)//2
            tmp=m*m
            if tmp==x:
                return m
            elif tmp<x:
                l=m+1
            elif tmp>x:
                r=m-1
        
        if l*l>x:
            return l-1
        return l
