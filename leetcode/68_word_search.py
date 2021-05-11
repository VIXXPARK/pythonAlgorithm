class Solution:
    def exist(self, board, word: str) -> bool:
        row=len(board);col=len(board[0])
        visited=[[False]*col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                if word[0]==board[i][j]:
                    visited[i][j]=True
                    if self.dfs(board,word[1:],i,j,row,col,visited):
                        return True
                    visited[i][j]=False
        return False
    
    def dfs(self,board,word,i,j,row,col,visited):
        dy=[1,-1,0,0]
        dx=[0,0,1,-1]
        if len(word)==0:
            return True
        for idx in range(4):
            fy,fx=i+dy[idx],j+dx[idx]
            if 0<=fy<row and 0<=fx<col:
                if board[fy][fx]==word[cur] and not visited[fy][fx]:
                    visited[fy][fx]=True
                    if self.dfs(board,word[1:],fy,fx,row,col,visited):
                        return True
                    visited[fy][fx]=False
        return False

#########################################################################################
class Solution:
    def exist(self, board, word: str) -> bool:
        def isValid(board, row, col):
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            return True
        
        def explore(board, row, col, s, visited):
            if not s:
                return True
            if isValid(board, row, col) and board[row][col] == s[-1] and (row, col) not in visited:
                visited.add((row, col))
                return (explore(board, row+1, col, s[:-1], visited) or
                explore(board, row-1, col, s[:-1], visited) or
                explore(board, row, col+1, s[:-1], visited) or
                explore(board, row, col-1, s[:-1], visited))
                visited.remove((row, col))
            return False
        
        rows = len(board)
        cols = len(board[0])
        
        for row in range(rows):
            for col in range(cols):
                if explore(board, row, col, word, set()):
                    return True
        return False

s=Solution()
print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED"))