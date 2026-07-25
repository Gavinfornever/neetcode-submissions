class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)
        while l<r:
            m=r+(l-r)//2
            if nums[m]>nums[-1]:
                l=m+1
            else:
                r=m
        pivot = l
        
        if pivot>=1 and target>=nums[0] and target<=nums[pivot-1]:
            l=0
            r=pivot-1
        else:
            l=pivot
            r=len(nums)-1
        
        while l<=r:
            m=r+(l-r)//2
            if target==nums[m]:
                return m
            elif target>nums[m]:
                l=m+1
            elif target<nums[m]:
                r=m-1
        return -1



