class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:return nums[0]
        res = -1
        dp = {}
        dp[0] = 1
        dp[-1] = 1
        for i in range(length):
            # dp[i] = max(nums[i]*dp[i-1], dp[i-1])
            if dp[i-1]==0:
                dp[i] = nums[i]
                res = max(res, dp[i])
                continue
            dp[i] = dp[i-1]*nums[i]
            if dp[i]<dp[i-1]:
                # res = dp[i-1]
                dp[i] = nums[i]
            else:
                # tmp*=nums[i]
                res = max(res, dp[i])
                # dp[i] = tmp
                

        return res



