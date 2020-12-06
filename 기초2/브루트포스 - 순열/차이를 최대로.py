import sys
N=int(input())
passing =[False]*(N+1)
li = list(map(int,sys.stdin.readline().split()))
li.sort()
st=[]
ret=0
def func(celi):
    global ret
    if celi==N:
        ans=0
        for k in range(N-1):
            ans+=abs(st[k]-st[k+1])
        ret=max(ans,ret)
        return
    for i in range(N):
        if not passing[i]:
            passing[i]=True
            st.append(li[i])
            func(celi+1)
            passing[i]=False
            st.pop()
func(0)
print(ret)
        

