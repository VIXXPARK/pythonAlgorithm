class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transponser(matrix)
        self.reverser(matrix)
        
    def transponser(self, matrix):
        lenMatrix = len(matrix)
        for i in range(lenMatrix):
            for j in range(i, lenMatrix):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

    def reverser(self, matrix):
        lenMatrix = len(matrix)
        for i in range(lenMatrix):
            for j in range(lenMatrix // 2):
                matrix[i][j], matrix[i][-j - 1] = matrix[i][-j - 1], matrix[i][j]