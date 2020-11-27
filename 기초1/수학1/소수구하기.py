import sys
x,y = map(int,sys.stdin.readline().split())
pri=[True]*1000000
pri[1]=False
for i in range(2,int((y+1)**0.5)+1):
   if pri[i]==True:
       for j in range(i*i,y+1,i):
           pri[j]=False
    
for i in range(x,y+1):
    if pri[i]:
        print(i)