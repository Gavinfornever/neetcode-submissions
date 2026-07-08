class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:return nums[0]
        res = max(nums)
        mn = 1
        mx = 1
        dp = {}
        dp[0] = 1
        dp[-1] = 1
        for i in range(length):
            if nums[i]==0:
                mx = 1
                mn = 1
            tmp = (nums[i]*mx, nums[i]*mn)
            mx = max(nums[i], tmp[0], tmp[1])
            mn = min(nums[i], tmp[0], tmp[1])
            res = max(mx, res)
                # l, r = nums[i]*mn, nums[i]*mx
                # mx=max(mx,r)
                # mx = max(mx, nums[i])
                # mn=min(mn,l)
            # else:
            #     l, r = nums[i]*mx, nums[i]*mn
            #     mx=max(mx,r)
            #     mn=min(mn,l)
            #     mn= min(mn, nums[i])

        return res



