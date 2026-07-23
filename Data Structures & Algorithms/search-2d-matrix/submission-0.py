class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix),  len(matrix[0])
        nums = rows*cols
        l, r = 0, nums - 1
        def getIndex(x):
            return x//cols, x%cols
        while l<=r:
            mid = r+(l-r)//2
            ml, mr = getIndex(mid)
            if matrix[ml][mr] == target:
                return True
            elif matrix[ml][mr] < target:
                l = mid+1
            elif matrix[ml][mr] > target:
                r = mid -1
        return False