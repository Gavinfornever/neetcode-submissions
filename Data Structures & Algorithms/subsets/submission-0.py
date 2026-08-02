class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            # if subset not in res:
            #     res.add(subset)
            if i==len(nums):
                res.append(subset.copy())
                return
            
            # decide to include nums[i]
            subset.append(nums[i])
            dfs(i+1)
            # decide not to include nums[i]
            subset.pop()
            dfs(i+1)

            # for x in nums:
            #     if x in subset:
            #         continue
            #     tmp = (x)
            #     subset = subset + tmp
            #     dfs(subset, step+1)
            #     subset= subset-tmp
        dfs(0)
        return res

