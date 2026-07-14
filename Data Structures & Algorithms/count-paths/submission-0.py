class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        directions = [[1,0],[0,1]]
        def dfs(x, y):
            nonlocal count
            if x>(m-1) or y>(n-1):
                return
            if x==(m-1) and y==(n-1):
                count += 1
            for d in directions:
                dfs(x+d[0], y+d[1])
        dfs(0, 0)
        return count



        