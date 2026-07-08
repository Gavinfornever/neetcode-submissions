class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        m = (l+r)//2
        # while l<r and m!=l and m!=r:
        while l<r:
            if nums[m]>nums[r]:
                l=m+1
                m=(l+r)//2
            elif nums[l]<nums[m]:
                r=m-1
                m=(l+r)//2
            else:
                break
        return nums[m]

