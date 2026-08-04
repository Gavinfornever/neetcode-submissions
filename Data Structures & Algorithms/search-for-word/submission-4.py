class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def dfs(i, x, y):
            if i==len(word):
                return True

            if x<0 or y<0 or x>=len(board) or y>=len(board[0]) \
                or board[x][y]!=word[i] or (x,y) in visited:
                return False
            
            visited.add((x,y))

            for dx, dy in [[0,1],[1,0],[-1,0],[0,-1]]:
                if dfs(i+1, x+dx, y+dy):
                    return True
            visited.remove((x,y))
            return False

        res = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                res = res or dfs(0, i, j)
        return res


