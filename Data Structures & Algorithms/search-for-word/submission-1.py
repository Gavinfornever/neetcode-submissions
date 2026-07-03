class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        res = False
        def dfs(i,j,step):
            res = False
            if step==(len(word)-1) and board[i][j]==word[step]:
                return True
            if board[i][j]=="#" or i<0 or i>=rows or j<0 or j>=rows or word[step]!=board[i][j]:
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
        
        return res





