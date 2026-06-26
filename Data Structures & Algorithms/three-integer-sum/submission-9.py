class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4 -1 -1 0 1 2
        res = set()
        nums = sorted(nums)
        for i, x in enumerate(nums):
            # print(x)
            l, r = i+1, len(nums)-1
            while l<r:
                sum3 = nums[l]+nums[r]+x
                # print(": ",x,nums[l],nums[r])
                # print("sum3: ",sum3)
                if sum3<0:
                    l+=1
                    # while l<r:
                    #     if nums[l]==nums[l-1]:
                    #         l+=1
                    #     else:
                    #         break
                elif sum3>0:
                    r-=1
                    # while l<r:
                    #     if nums[r]==nums[r+1]:
                    #         r-=1
                    #     else:
                    #         break
                else:
                    tmp = (nums[l], nums[r], x)
                    res.add(tmp)
                    l+=1

        return list(res)

