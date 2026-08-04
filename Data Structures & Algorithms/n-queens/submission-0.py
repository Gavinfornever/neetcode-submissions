class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def check(row, col):
            # check col
            for i in range(row):
                if board[i][col]=="Q":
                    return False
            # check up left
            r, c = row-1, col-1
            while r>=0 and c>=0:
                if board[r][c]=="Q":
                    return False
                r-=1
                c-=1

            # check up right
            r, c = row-1, col+1
            while r>=0 and c<len(board[0]):
                if board[r][c]=="Q":
                    return False
                r-=1
                c+=1
            return True

        def dfs(row):
            if row==n:
                res.append( [ "".join(r) for r in board  ]  )
                return
            
            for col in range(n):
                if check(row, col):
                    board[row][col] = 'Q'
                    dfs(row+1)
                    board[row][col] = '.'
        dfs(0)
        return res

