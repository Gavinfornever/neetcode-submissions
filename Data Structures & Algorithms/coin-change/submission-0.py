class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:return 0
        dp = {}
        dp[0] = 0
        for x in range(1, amount+1):
            dp[x] = float("inf")
            for c in coins:
                # if c>
                if x-c<0:
                    continue
                dp[x] = min(dp[x], dp[x-c]+1)
                # if x-c>=0:
                #     dp[x] = dp[x-c]+1
                # else:
                #     dp[x] = dp[x-1]+1
        if dp[amount] == float("inf"):return -1
        return dp[amount]
        # dp[x] = dp[x-i] + 1
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 3
        # dp[4] = 4
        # dp[5] = 2
        # dp[x] = min(dp[x-coins[0]]+coins[0], dp[x-c]+1)


        