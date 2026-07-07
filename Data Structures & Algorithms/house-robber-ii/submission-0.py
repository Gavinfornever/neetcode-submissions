class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 1:return nums[0]

        def dp(x):
            length = len(x)
            if length == 1:return x[0]
            dic = {}
            dic[0] = x[0]
            dic[1] = max(x[0], x[1])
            for i in range(2, length):
                dic[i] = max(dic[i-2]+x[i], dic[i-1])
            return dic[length-1]

        return max(dp(nums[:length-1]), dp(nums[1:length]))

        

        
        
        



