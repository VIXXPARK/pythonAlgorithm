from collections import deque
import itertools
def solution(m, n, board):
    answer = 0
    lstBoard=[]
    for i in range(m):
        lstBoard.append(list(board[i]))
    lstBoard=list(map(list,zip(*lstBoard)))
    visited=[[1 for _ in range(m)]for _ in range(n)]
    cnt=1
    while cnt:
        for i in range(0,n-1):
            for j in range(0,m-1):
                if lstBoard[i][j]!='*' and  lstBoard[i][j]==lstBoard[i+1][j] and lstBoard[i][j]==lstBoard[i+1][j+1] and lstBoard[i][j]==lstBoard[i][j+1]:
                    visited[i][j]=0
                    visited[i+1][j]=0
                    visited[i+1][j+1]=0
                    visited[i][j+1]=0
        for i in range(n):
            val = list(itertools.compress(lstBoard[i],visited[i]))
            for _ in range(0,m-len(val)):
                val.insert(0,'*')
                cnt+=1
            lstBoard[i]=val[:]
        answer+=cnt-1
        visited=[[1 for _ in range(m)]for _ in range(n)]
        if cnt==1:
            cnt=0 
        else:
            cnt=1    
    return answer

print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))