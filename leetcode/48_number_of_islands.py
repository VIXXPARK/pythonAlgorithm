from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lenY=len(grid)
        lenX=len(grid[0])
        visited=[[False for _ in range(lenX)] for _ in range(lenY)]
        dy=[1,-1,0,0]
        dx=[0,0,1,-1]
        def bfs(y,x):
            q=deque()
            q.append([y,x])
            visited[y][x]=True
            while q:
                fy,fx=q.popleft()
                for i in range(4):
                    gy=fy+dy[i]
                    gx=fx+dx[i]
                    if 0<=gy<lenY and 0<=gx<lenX:
                        if grid[gy][gx]=="1" and not visited[gy][gx]:
                            visited[gy][gx]=True
                            q.append([gy,gx])
        
        ans=0
        for i in range(lenY):
            for j in range(lenX):
                if grid[i][j]=="1" and not visited[i][j]:
                    ans+=1
                    bfs(i,j)
        return ans

####################################################################################

