class Solution:
    def climbStairs(self, n: int) -> int:
        # c(n) = 1, c(n-1)
        # c(n) = 2, c(n-2)
        # c(n-1) = 1, c(n-2)
        # c(n-1) = 2, c(n-3)
        if n==1:
            return 1
        elif n==2:
            return 2
        return max(1 + self.climbStairs(n-1), 2 + self.climbStairs(n-2))
