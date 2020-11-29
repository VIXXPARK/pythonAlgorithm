import sys
def gcd(left,right):
    if right==0:
        return left
    return gcd(right,left%right)

N,S = map(int,sys.stdin.readline().rstrip().split())
dong = list(map(int,sys.stdin.readline().split()))
ans=int(abs(S-dong[0]))
for i in range(1,len(dong)):
    ans=gcd(int(abs(S-dong[i])),ans)
print(ans)

