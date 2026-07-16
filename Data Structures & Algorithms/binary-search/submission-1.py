class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        l, r = 0, length-1
        m = 0
        while l<=r:
            # m = (l+r)//2
            m = l + (r-l)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l = m+1
            elif nums[m]>target:
                r = m-1
        return -1    


