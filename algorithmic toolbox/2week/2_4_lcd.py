def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)
a,b=map(int,input().split())
num=gcd(a,b)
print(a*b//num)