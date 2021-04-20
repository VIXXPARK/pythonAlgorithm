class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
            import bisect
            row,col=len(matrix),len(matrix[0])
            for i in range(row):
                lower_bound=bisect.bisect_left(matrix[i],target,0,(col))
                if lower_bound<col and matrix[i][lower_bound]==target:
                    return True
            return False