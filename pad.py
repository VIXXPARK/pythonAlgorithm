class Solution:
    def exist(self, board, word: str) -> bool:
        startChar=word[0]
        row=len(board);col=len(board[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if startChar==board[i][j]:
                    visited[i][j]=True
                    if self.dfs(board,word,i,j,row,col,visited,1):
                        return True
                    visited[i][j]=False
        return False
    
    def dfs(self,board,word,i,j,row,col,visited,cur):
        dy=[1,-1,0,0]
        dx=[0,0,1,-1]
        if len(word)==cur:
            return True
        for idx in range(4):
            fy,fx=i+dy[idx],j+dx[idx]
            if 0<=fy<row and 0<=fx<col:
                if board[fy][fx]==word[cur] and not visited[fy][fx]:
                    visited[fy][fx]=True
                    if self.dfs(board,word,fy,fx,row,col,visited,cur+1):
                        return True
                    visited[fy][fx]=False
        return False

s= Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB"))