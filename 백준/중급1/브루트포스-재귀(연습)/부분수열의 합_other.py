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

n = int(input())
a = list(map(int,input().split()))
c = [False]*(n*100000+10)
def go(i, sum):
    if i == n:
        c[sum] = True
        return
    go(i+1,sum+a[i])
    go(i+1,sum)
go(0,0)
i = 1
while True:
    if c[i] == False:
        break
    i += 1
print(i)