import sys
input=sys.stdin.readline
N=int(input())
li=list(map(int,input().rstrip().split()))
visited=[False]*N
li.sort()
sumList=[]
maxNum=2000000
numList=[False]*(maxNum)
numList[0]=True
def func(ceil,aim,sum,ans):
    if ceil==aim:
        return
    for i in range(len(li)):
        if not ans:
            visited[i]=True
            sum+=li[i]
            numList[sum]=True
            ans.append(i)
            func(ceil+1,aim,sum,ans)
            ans.pop()
            sum-=li[i]
            visited[i]=False
        elif not visited[i] and ans[-1]<i:
            visited[i]=True
            sum+=li[i]
            ans.append(i)
            numList[sum]=True
            func(ceil+1,aim,sum,ans)
            ans.pop()
            sum-=li[i]
            visited[i]=False
        
func(0,len(li),0,[])
cnt=1
while True:
    if numList[cnt]==False:
        print(cnt)
        break
    else:
        cnt+=1

##나중에 더 빠른 코드 보기