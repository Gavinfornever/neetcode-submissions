class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[n] = 1
        dp[n-1] = 1
        dp[n-2] = 2
        for i in range(n-3, 1, -1):
            # if i+2 < n:
            dp[i] = dp[i+1]+dp[i+2]
            # else:
            #     if i+1< n:
            #         dp[i] = dp[i+1]
            #     else:
            #         dp[i] = 1
        return dp[1]
