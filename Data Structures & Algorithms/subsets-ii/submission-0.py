class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # vis = [False]*len(nums)
        res = set()
        nums.sort()
        cur = []
        def dfs(i, cur):
            if i==len(nums):
                res.add(tuple(cur))
                return
            
            cur.append(nums[i])
            dfs(i+1, cur)
            cur.pop()
            dfs(i+1, cur)
        
        dfs(0, cur)
        return [list(x) for x in res]


