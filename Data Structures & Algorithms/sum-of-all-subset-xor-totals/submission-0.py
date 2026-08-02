class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0
        subset = []
        def dfs(i):
            nonlocal res
            if i==len(nums):
                tmp = 0
                for x in subset:
                    tmp = tmp^x
                res += tmp
                return
            
            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res

