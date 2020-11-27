import sys
pri=[True]*1000001
pri[0]=False
pri[1]=False
for i in range(2,int((1000000+1)**0.5)):
   if pri[i]==True:
       for j in range(i*i,1000000+1,i):
           pri[j]=False
pri[2]=False

while(True):
    val=int(sys.stdin.readline().rstrip())
    if val==0:
        break
    x,y,rx,ry,ans=0,0,0,0,-1
    for i in range(3,(val//2)+1):
        x=i
        y=val-x
        if pri[x]==True and pri[y]==True:
            if ans<y-x:
                rx,ry=x,y
                ans=y-x
                break
    if rx!=0 and ry!=0:
        print(val,end=' ')
        print("=",end=' ')
        print(rx,end=' ')
        print("+ ",end='')
        print(ry)
    else:
        print("Goldbach's conjecture is wrong.")

    