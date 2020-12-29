import sys
N = int(input())
col=[False]*20
diag1=[False]*50
diag2=[False]*50
cnt=0
def func(y):
    global cnt
    if y==N:
        cnt+=1
        return
    else:
        for x in range(N):
            if col[x] or diag1[x+y] or diag2[x-y+N-1]:
                continue
            col[x]=diag1[x+y]=diag2[x-y+N-1]=1
            func(y+1)
            col[x]=diag1[x+y]=diag2[x-y+N-1]=0
func(0)
print(cnt)