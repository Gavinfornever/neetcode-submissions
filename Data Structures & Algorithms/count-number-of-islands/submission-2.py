class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        rows= len(grid)
        cols= len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            visited.add((i,j))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r = row+dr
                    c = col+dc
                    if r>=0 and r<rows and c>=0 and c<cols \
                        and grid[r][c]=="1" and (r,c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))
        
        def dfs(r, c):
            if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]=="0"):
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                row = r+dr
                col = c+dc
                dfs(row, col)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited: # new island found
                    dfs(i, j)
                    islands+=1
        return islands