class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, sm, lst):
            if sm==target:
                res.append(lst.copy())
                return 
            
            elif sm>target or i >=len(nums):
                return None
                # for m in nums:
                #     dfs(m, sm, lst)
            else:
                lst.append(nums[i])
                dfs(i, sm+nums[i], lst)
                lst.pop()
                dfs(i+1, sm, lst)

                # for m in nums:
                #     # dfs()
                #     dfs(m, sm, lst)
                    # lst.remove(x)
                    # lst.pop()
                    # sm-=x
            # sm-=nums[i]
            # lst.pop()
            return 
        dfs(0,0,[])
        return res
