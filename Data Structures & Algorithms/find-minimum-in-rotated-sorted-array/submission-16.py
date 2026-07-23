class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1

        while l<r:
            m = r + (l-r)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        return nums[l]


        # mn = nums[0]
        # while l<=r:
            
        #     if nums[l]<nums[r]:
        #         mn  = min(mn, nums[l])
        #         break
            
        #     m = r + (l-r)//2
        #     mn  = min(mn, nums[m])
        #     if nums[m]>=nums[l]:
        #         l=m+1
        #     else:
        #         r=m-1
        # return mn




