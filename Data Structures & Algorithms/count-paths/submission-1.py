class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        # directions = [[1,0],[0,1]]
        memo = {}
        def dfs(x, y):
            if x>(m-1) or y>(n-1):
                return 0
            if x==(m-1) and y==(n-1):
                return 1
            if (x,y) in memo:
                return memo[(x,y)]
            # for d in directions:
            #     dfs(x+d[0], y+d[1])
            memo[(x,y)] = dfs(x+1,y)+dfs(x,y+1)
            return memo[(x,y)]
        
        return dfs(0, 0)



        