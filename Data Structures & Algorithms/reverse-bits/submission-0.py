class Solution:
    def reverseBits(self, n: int) -> int:
        
        bits = []
        while n:
            bits.append(n%2)
            n = n>>1
        
        res = 0
        for i in range(len(bits)):
            res += bits[i]*pow(2, 31-i)

        return res


