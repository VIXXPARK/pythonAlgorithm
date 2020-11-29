import sys
num = int(sys.stdin.readline().rstrip())
li = list(map(int,sys.stdin.readline().rstrip().split()))
pri=[]
pri.append(0)
pri.append(0)

for i in range(2,1001):
    val=1
    for j in range(2,i):
        if i%j==0:
            val=0
            break
    pri.append(val)
ans=0
for i in li:
    ans+=pri[i]
print(ans)
