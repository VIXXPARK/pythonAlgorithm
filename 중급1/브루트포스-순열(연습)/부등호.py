import sys
N=int(sys.stdin.readline().rstrip())
sign=list(sys.stdin.readline().rstrip().split())
visited=[False]*10
iteration=[]
li=[]
def func(celi,aim):
    global li
    if celi==aim:
        iteration.append(list(li))
        return
    
    for i in range(10):
        if not li:
            if not visited[i]:
                visited[i]=True
                li.append(i)
                func(celi+1,aim)
                li.pop()
                visited[i]=False
        else:
            if sign[celi-1]=='<':
                if li[-1]<i and not visited[i]:
                    visited[i]=True
                    li.append(i)
                    func(celi+1,aim)
                    li.pop()
                    visited[i]=False
            else:
                if li[-1]>i and not visited[i]:
                    visited[i]=True
                    li.append(i)
                    func(celi+1,aim)
                    li.pop()
                    visited[i]=False

func(0,N+1)
print(''.join(map(str,iteration[-1])))
print(''.join(map(str,iteration[0])))
