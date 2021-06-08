class Solution:
    def maximalRectangle(self, matrix) -> int:
        if matrix==[]: return 0
        row=len(matrix)
        col=len(matrix[0])
        row_dp=[[0]*(col+1) for _ in range(row+1)] ## 세로로 된 길이를 저장하면서 확인하는 형식으로 
        ans=0
        for i in range(1,row+1):
            for j in range(1,col+1):
                if matrix[i-1][j-1]=="1":
                    row_dp[i][j]=row_dp[i-1][j]+1
        for i in range(1,row+1):
            for j in range(1,col+1):
                height=row_dp[i][j]
                for k in range(j,col+1):
                    height=min(height,row_dp[i][k])
                    if row_dp[i][k]!=0:
                        ans=max(ans,(k-j+1)*height)
                    else:
                        break         
        return ans 

######################################################
def maximalRectangle(self, matrix):
    if not matrix or not matrix[0]:
        return 0
    n = len(matrix[0])
    height = [0] * (n + 1)
    ans = 0
    for row in matrix:
        for i in range(n):
            height[i] = height[i] + 1 if row[i] == '1' else 0
        stack = [-1]
        for i in range(n + 1):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - 1 - stack[-1]
                ans = max(ans, h * w)
            stack.append(i)
    return ans