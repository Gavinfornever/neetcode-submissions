class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        # dp[len(nums)-1] = 1
        for i in range(len(nums)-1, -1, -1):# i=5
            # print(i)
            for j in range(i+1, len(nums)):  # j=6
                # print("j: ", j)
                if nums[i]<nums[j]:
                    dp[i] = max(dp[j]+1, dp[i])
                    # break
            # if nums[i]<nums[i+1]:
            #     dp[i] = dp[i+1] + 1
            # else:
                
        
        return max(dp)



