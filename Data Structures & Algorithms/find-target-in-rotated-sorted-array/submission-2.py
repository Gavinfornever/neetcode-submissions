class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r =  0, len(nums)-1
        while l<r:
            m  = r+(l-r)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        cut = l # this is the min element
        def findTarget(l,r):
            while l<=r:
                m = r+(l-r)//2
                if nums[m]==target:
                    return m
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return -1
        left = findTarget(0,cut-1)
        right = findTarget(cut, len(nums)-1)
        if left != -1: return left
        if right != -1: return right
        return -1

