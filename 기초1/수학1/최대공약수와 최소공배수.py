import sys
a,b=map(int,sys.stdin.readline().rstrip().split())
def gcd(x,y):
    if y==0:
        return x
    return gcd(y,x%y)
val = gcd(a,b)
val2 = (a/val)*(b)
print(val)
print(int(val2))