class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        vis = [False]*len(nums)
        res = set()
        cur = []
        def dfs():
            if len(cur)==len(nums):
                res.add(tuple(cur))
                return
            # run every element
            for i in range(len(nums)):
                if not vis[i]:
                    vis[i]=True
                    cur.append(nums[i])
                    dfs()
                    vis[i]=False
                    cur.pop()
                    # dfs()
        dfs()
        return [list(x) for x in res]
