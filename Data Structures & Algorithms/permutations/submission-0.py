class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        cur = []
        def dfs():
            if len(cur)==len(nums):
                res.append(cur.copy())
                return
            # if nums[i] in cur:
            #     return
            
            
            for x in range(len(nums)):
                if nums[x] not in cur:
                    cur.append(nums[x])
                    dfs()
                    cur.pop()
            # for 
            # cur.append(nums[i])
            # dfs(i+1)
            # cur.pop()
            # dfs(i+1)
        # dfs(0)
        # for i in range(len(nums)):
        #     dfs(i)
        dfs()
        return res

