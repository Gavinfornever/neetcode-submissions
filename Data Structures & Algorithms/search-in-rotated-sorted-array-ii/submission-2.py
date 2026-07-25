class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l,r=0,len(nums)
        while l<r:
            m=r+(l-r)//2
            if nums[m]>=nums[-1]:
                l=m+1
            else:
                r=m
        pivot = l

        # now decide which side
        if pivot>=1 and target>=nums[0] and target<=nums[pivot-1]:
            r=pivot-1
            l=0
        else:
            l=pivot
            r=len(nums)-1
        
        # now find the target
        while l<=r:
            m=r+(l-r)//2
            if nums[m]==target:
                return True
            elif nums[m]>target:
                r=m-1
            elif nums[m]<target:
                l=m+1
        return False

