import sys
pri = [True]*1000001
pri[0]=False
pri[1]=False
for i in range(2,int((1000001)**0.5)):
    if pri[i]==True:
        for j in range(i*i,1000001,i):
            pri[j]=False
for _ in range(int(sys.stdin.readline().rstrip())):
    val=int(sys.stdin.readline().rstrip())
    ans=0
    for x in range(3,int((val+1)//2)+1):
        if pri[x]==True and pri[val-x]==True:
            ans+=1
    print(ans)
