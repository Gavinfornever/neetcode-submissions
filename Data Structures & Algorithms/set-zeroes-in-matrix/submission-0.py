class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visited = set()
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] == 0 and (i,j) not in visited:
                    for x in range(0, len(matrix)):
                        matrix[x][j] = 0
                        visited.add((x, j))
                    for x in range(0, len(matrix[0])):
                        matrix[i][x] = 0
                        visited.add((i, x))
        

        