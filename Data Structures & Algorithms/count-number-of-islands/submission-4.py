class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        directions = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="0":
                    continue
                num+=1
                q = []
                q.append((i,j))
                
                while q:
                    m, n = q.pop()
                    grid[m][n] = "0"
                    for x,y in directions:
                        if m+x>=0 and m+x<len(grid) and n+y>=0 and n+y<len(grid[0]) and \
                        grid[m+x][n+y]=="1":
                            q.append((m+x, n+y))
        
        return num







