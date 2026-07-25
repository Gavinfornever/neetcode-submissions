class Solution:
    def findMin(self, nums: List[int]) -> int:
        mn= nums[0]
        l,r=0,len(nums)-1
        while l<=r:
            m=r+(l-r)//2
            mn=min(mn, nums[m])
            mn=min(mn, nums[l])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1
        return mn

