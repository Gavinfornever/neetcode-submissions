class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = (l+r)//2
        while l<r:
            if nums[m]>nums[r]:
                l=m
                m=(l+r)//2
            else:
                break
        return nums[m]

