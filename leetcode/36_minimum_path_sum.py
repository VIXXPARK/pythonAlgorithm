class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        col=len(grid)
        row=len(grid[0])
        for i in range(col):
            for j in range(row):
                if i==0:
                    if j==0:
                        continue
                    else:
                        grid[i][j]=grid[i][j-1]+grid[i][j]
                elif j==0:
                    grid[i][j]=grid[i-1][j]+grid[i][j]
                else:
                    grid[i][j]=min(grid[i-1][j],grid[i][j-1])+grid[i][j]
        return grid[col-1][row-1]