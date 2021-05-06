class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows=len(matrix)
        cols=len(matrix[0])
        if rows==0:
            return 0
        dp=[[0]*(cols+1) for _ in  range(rows+1)]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]=="1":
                    dp[r+1][c+1]=min(dp[r][c],dp[r][c+1],dp[r+1][c])+1
        
        return max(map(max, dp))**2

################################################################################
class Solution:
    def maximalSquare(self, A):
        for i in range(len(A)):
            for j in range(len(A[i])):
                A[i][j] = int(A[i][j])
                if A[i][j] and i and j:
                    A[i][j] = min(A[i-1][j], A[i-1][j-1], A[i][j-1]) + 1
        return len(A) and max(map(max, A)) ** 2

#################################################################################
class Solution:
    def maximalSquare(self, A):
        for i, r in enumerate(A):
            r = A[i] = map(int, r)
            for j, c in enumerate(r):
                if i * j * c:
                    r[j] = min(A[i-1][j], r[j-1], A[i-1][j-1]) + 1
        return max(map(max, A + [[0]])) ** 2

#################################################################################

class Solution:
    def maximalSquare(self, A):
        area = 0
        if A:
            p = [0] * len(A[0])
            for row in A:
                s = map(int, row)
                for j, c in enumerate(s[1:], 1):
                    s[j] *= min(p[j-1], p[j], s[j-1]) + 1
                area = max(area, max(s) ** 2)
                p = s
        return area