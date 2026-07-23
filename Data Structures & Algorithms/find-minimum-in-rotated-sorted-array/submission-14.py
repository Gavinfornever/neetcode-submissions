class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums)-1
        mn = nums[0]
        while l<=r:
            
            if nums[l]<nums[r]:
                mn  = min(mn, nums[l])
                break
            
            m = r + (l-r)//2
            mn  = min(mn, nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r=m-1

            # x = nums[mid]
            # if x>nums[l] and x<nums[r]:
            #     r = mid
            # # elif x>nums[l] and x>nums[r]:
            # #     continue
            # elif x<nums[l] and x<nums[r]:
            #     r=mid
            # elif x<nums[l] and x>nums[r]:
        
        return mn




