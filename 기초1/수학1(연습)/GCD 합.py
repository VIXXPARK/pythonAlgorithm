import sys

def gcd(left,right):
    if right==0:
        return left
    return gcd(right,left%right)

for _ in range(int(sys.stdin.readline().rstrip())):
    ans=0
    cmd = list(map(int,sys.stdin.readline().rstrip().split()))
    del cmd[0]
    for x in range(0,len(cmd)):
        for y in range(x+1,len(cmd)):
            Big=max(cmd[x],cmd[y])
            Small=min(cmd[x],cmd[y])
            ans+=gcd(Big,Small)
    print(ans)

