import sys
def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)
testcase = int(sys.stdin.readline().rstrip())
for _ in range(testcase):
    a,b=map(int,sys.stdin.readline().strip().split())
    val = gcd(a,b)
    val2 = (a/val)*(b)
    print(int(val2))