class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        res = nums[0]
        # m = (l+r)//2
        while l<=r:
            if nums[l]<nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l+r)//2
            res = min(nums[m], res)
            if nums[m]<nums[l]:
                r = m-1
            else:
                l = m+1
        return res
        # while l<r and m!=l and m!=r:
        # while l<r:
        #     if nums[m]>nums[r] and nums[m]>nums[l]:
        #         l=m+1
        #         m=(l+r)//2
        #     elif nums[m]>nums[l] and nums[m]<nums[r]:
        #         r=m-1
        #         m=(l+r)//2
        #     elif nums[m]<nums[l] and nums[m]<nums[r]:
        #         r=m-1
        #         m=(l+r)//2
        #     # elif nums[m]<nums[l] and nums[m]>nums[r]:
        #     #     l=m+1
        #     #     m=(l+r)//2
        #     else:
        #         break
        # return nums[m]

