import sys
def func(li,st,passing,celi,N):
    if celi==N:
        print(' '.join(st))
        return
    for i in range(len(li)):
        if not st:
            passing[i]=True
            st.append(str(li[i]))
            func(li,st,passing,celi+1,N)
            passing[i]=False
            st.pop()
        elif not passing[i] and int(st[-1])<li[i]:
            passing[i]=True
            st.append(str(li[i]))
            func(li,st,passing,celi+1,N)
            passing[i]=False
            st.pop()


while True:
    li=list(map(int,sys.stdin.readline().rstrip().split()))
    if li[0]==0:
        break
    N=li[0]
    del li[0]
    st=[]
    passing = [False]*N
    func(li,st,passing,0,6)
    print()