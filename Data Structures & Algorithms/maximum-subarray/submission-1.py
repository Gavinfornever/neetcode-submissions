class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l=0
        curSum = 0
        res = float('-inf')
        while l<len(nums):
            if curSum+nums[l] < 0:
                l+=1
                res = max(res, curSum)
                curSum = 0
                continue
            curSum = curSum+nums[l]
            res = max(res, curSum)
            l+=1
        
        return res