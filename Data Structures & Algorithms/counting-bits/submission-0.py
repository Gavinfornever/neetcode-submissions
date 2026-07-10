class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBit(n):
            res = 0
            while n:
                n = n & (n-1)
                res+=1
            return res
        res = []
        for i in range(0, n+1):
            res.append(countBit(i))
        return res


