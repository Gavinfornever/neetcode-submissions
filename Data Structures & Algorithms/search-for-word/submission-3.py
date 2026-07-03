class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        def dfs(i,j,step):
            res = None
            if step==len(word):
                return True
            if  i<0 or i>=rows or j<0 or j>=cols or board[i][j]=="#" or word[step]!=board[i][j]:
                return False

            board[i][j] = "#"
            for dx, dy in directions:
                res = res or dfs(dx+i, dy+j, step+1)
            board[i][j] = word[step]
            return res

        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True
        
        return False





