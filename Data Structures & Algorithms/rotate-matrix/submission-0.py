class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        length = len(matrix)
        if length == 1:return
        for i in range(length//2):
            for j in range(length):
                tmp = matrix[i][j]
                matrix[i][j]  = matrix[length-1-i][j]
                matrix[length-1-i][j] = tmp

        for i in range(length):
            for j in range(i+1, length):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp

